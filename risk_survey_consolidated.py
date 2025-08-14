
import random
import json
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional

import pandas as pd
import streamlit as st

# ---------- Page Setup ----------
st.set_page_config(page_title="Risk Preference Survey", layout="wide")

st.title("Risk Preference Survey")

# Optional visible build tag so you always know which file is live
st.caption("build: consolidated-robust-1.0")


# ---------- Utilities ----------
def format_money(x: float) -> str:
    return f"${x:,.2f}"


def describe_prospect(prospect: Dict) -> str:
    """Readable 2-outcome description with 'win/lose nothing' as appropriate."""
    outs = prospect.get("outcomes", [])
    probs = prospect.get("probabilities", [])
    if len(outs) != 2 or len(probs) != 2:
        return prospect.get("description", "")
    o1, o2 = outs
    p1, p2 = probs

    def zero_phrase():
        return "win nothing" if max(o1, o2) > 0 else "lose nothing"

    def phr(p, x):
        if x == 0:
            return f"{int(p*100)}% chance to {zero_phrase()}"
        verb = "win" if x > 0 else "lose"
        return f"{int(p*100)}% chance to {verb} ${abs(x):,.0f}"

    # Keep the order consistent with provided probabilities
    return f"{phr(p2, o2)}, {phr(p1, o1)}"


def expected_value(prospect: Dict) -> float:
    outs = prospect["outcomes"]
    probs = prospect["probabilities"]
    return outs[0]*probs[0] + outs[1]*probs[1]


def check_consistency(choices: List[Optional[str]], amounts: List[float]) -> Optional[str]:
    """Return an error string if choices violate monotonicity; else None.
       amounts are descending (largest first)."""
    # If chose gamble at some amount i, must choose gamble for all smaller amounts (j > i)
    for i, ch in enumerate(choices):
        if ch == "prospect":
            for j in range(i+1, len(choices)):
                if choices[j] == "sure":
                    return "Choices are inconsistent: chose gamble at a higher sure amount but chose sure at a lower amount."
        if ch == "sure":
            for j in range(0, i):
                if choices[j] == "prospect":
                    return "Choices are inconsistent: chose sure at a lower sure amount but chose gamble at a higher amount."
    return None


def check_monotonic_violation(choices: List[Optional[str]], amounts: List[float], new_choice: str, idx: int) -> Tuple[bool, str]:
    """
    Return (violation: bool, message: str). `amounts` is descending (largest first).
    Monotonicity (Tversky & Kahneman, 1992):
      - If you prefer the gamble over a sure amount X, you must also prefer it over any smaller sure amount.
      - If you prefer a sure amount X over the gamble, you must also prefer any larger sure amount.
    """
    temp = list(choices)
    temp[idx] = new_choice

    for i, ch in enumerate(temp):
        if ch is None:
            continue

        # If you choose the gamble at amount[i], you must choose it for all smaller amounts (rows below, j > i)
        if ch == "prospect":
            for j in range(i + 1, len(temp)):
                if temp[j] == "sure":
                    msg = (
                        "Monotonicity violation.\n\n"
                        f"You chose the gamble instead of {format_money(amounts[i])}, "
                        f"but also chose a sure amount of {format_money(amounts[j])} on a lower row.\n\n"
                        "Monotonicity (Tversky & Kahneman, 1992): "
                        "If a gamble is better than some amount of money, it should be better than any smaller amount."
                    )
                    return True, msg

        # If you choose sure at amount[i], you must choose sure for all larger amounts (rows above, j < i)
        if ch == "sure":
            for j in range(0, i):
                if temp[j] == "prospect":
                    msg = (
                        "Monotonicity violation.\n\n"
                        f"You chose a sure amount of {format_money(amounts[i])}, "
                        f"but chose the gamble over a larger sure amount of {format_money(amounts[j])} on an upper row.\n\n"
                        "Monotonicity (Tversky & Kahneman, 1992): "
                        "If a certain amount is better than the gamble, any larger amount should also be better."
                    )
                    return True, msg

    return False, ""


def compute_certainty_equivalent(choices: List[str], amounts: List[float]) -> float:
    """Compute CE as midpoint between the switch: last 'sure' (higher) and first 'prospect' (lower).
       If all sure -> CE = max amount; if all prospect -> CE = min amount."""
    last_sure_idx = None
    first_prospect_idx = None
    for i, ch in enumerate(choices):
        if ch == "sure":
            last_sure_idx = i
        if ch == "prospect" and first_prospect_idx is None:
            first_prospect_idx = i

    if last_sure_idx is None and first_prospect_idx is None:
        # Shouldn't happen if all rows answered
        return amounts[-1]

    if last_sure_idx is None:
        # All prospect
        return amounts[-1]
    if first_prospect_idx is None:
        # All sure
        return amounts[0]

    # CE between the two boundary amounts
    high = amounts[last_sure_idx]
    low = amounts[first_prospect_idx]
    return round((high + low) / 2.0, 2)


def linear_space_desc(high: float, low: float, n: int = 7) -> List[float]:
    """Return n numbers from high down to low (inclusive), descending."""
    if n == 1:
        return [round(high, 2)]
    step = (high - low) / (n - 1)
    arr = [round(high - k*step, 2) for k in range(n)]
    return arr


def generate_sure_amounts(prospect: Dict, phase: int, phase1_choices: Optional[List[str]] = None) -> List[float]:
    outs = prospect["outcomes"]
    probs = prospect["probabilities"]
    domain = "gain" if max(outs) > 0 else "loss"

    max_abs = max(abs(outs[0]), abs(outs[1]))
    if phase == 1:
        # Phase 1: broad window around EV, descending
        # Gains: from 90% of max to 10% of max; Losses: negative values with same magnitudes
        hi = 0.9 * max_abs
        lo = 0.1 * max_abs
        arr = linear_space_desc(hi, lo, 7)
        if domain == "loss":
            arr = [-abs(x) for x in arr]  # negative numbers
        return arr

    # Phase 2: zoom in based on phase1 pattern
    # Determine bounds: highest sure-accepted and lowest gamble-accepted
    if not phase1_choices:
        # fallback: just compress Phase 1
        base = generate_sure_amounts(prospect, phase=1)
        mid_hi = base[1]
        mid_lo = base[-2]
        return linear_space_desc(mid_hi, mid_lo, 7)

    # Find last 'sure' and first 'prospect'
    last_sure = None
    first_prospect = None
    for i, ch in enumerate(phase1_choices):
        if ch == "sure":
            last_sure = i
        if ch == "prospect" and first_prospect is None:
            first_prospect = i

    base = generate_sure_amounts(prospect, phase=1)
    if last_sure is None and first_prospect is None:
        # No info: just compress phase 1
        return linear_space_desc(base[1], base[-2], 7)

    if last_sure is None:
        # All prospect -> focus near low end
        return linear_space_desc(base[-3], base[-1], 7)
    if first_prospect is None:
        # All sure -> focus near high end
        return linear_space_desc(base[0], base[2], 7)

    hi = base[last_sure]     # sure boundary (higher amount)
    lo = base[first_prospect]  # gamble boundary (lower amount)
    # Make sure hi >= lo; if inverted because of noise, swap
    if domain == "gain":
        if lo > hi:
            hi, lo = lo, hi
    else:
        # For losses, numbers are negative; "hi" is less negative (closer to zero)
        if lo > hi:  # e.g., -30 (lo) > -50 (hi) -> swap to have hi = -30, lo = -50
            hi, lo = lo, hi
    return linear_space_desc(hi, lo, 7)


def risk_attitude_from_ce(ce: float, ev: float) -> str:
    if ce < ev:
        return "Risk Averse"
    if ce > ev:
        return "Risk Seeking"
    return "Risk Neutral"


# ---------- Prospects (10 problems) ----------
# A simple fixed set: 5 gains, 5 losses
PROSPECTS = [
    {"outcomes": [0, 150], "probabilities": [0.9, 0.1], "description": "10% to win 150, else 0"},   # EV 15
    {"outcomes": [0, 100], "probabilities": [0.75, 0.25], "description": "25% to win 100, else 0"}, # EV 25
    {"outcomes": [0, 200], "probabilities": [0.5, 0.5], "description": "50% to win 200, else 0"},   # EV 100
    {"outcomes": [0, 300], "probabilities": [0.67, 0.33], "description": "33% to win 300, else 0"}, # ~99
    {"outcomes": [0, 50],  "probabilities": [0.2, 0.8], "description": "80% to win 50, else 0"},    # 40
    # Losses
    {"outcomes": [0, -100], "probabilities": [0.5, 0.5], "description": "50% to lose 100, else 0"}, # -50
    {"outcomes": [0, -150], "probabilities": [0.9, 0.1], "description": "10% to lose 150, else 0"}, # -15
    {"outcomes": [0, -200], "probabilities": [0.75, 0.25], "description": "25% to lose 200, else 0"},# -50
    {"outcomes": [0, -50],  "probabilities": [0.2, 0.8], "description": "80% to lose 50, else 0"},   # -40
    {"outcomes": [0, -300], "probabilities": [0.67, 0.33], "description": "33% to lose 300, else 0"},# -99
]


# ---------- Session State Init ----------
def init_state():
    if "started" not in st.session_state:
        st.session_state.started = False
        st.session_state.name = ""
        st.session_state.age = None

    if "prospects" not in st.session_state:
        # Randomize order but keep both domains mixed
        random.seed()  # remove for reproducibility
        st.session_state.prospects = random.sample(PROSPECTS, k=len(PROSPECTS))

    if "index" not in st.session_state:
        st.session_state.index = 0  # problem index
    if "phase" not in st.session_state:
        st.session_state.phase = 1  # 1 or 2
    if "current_choices" not in st.session_state:
        st.session_state.current_choices = [None] * 7  # 'prospect' or 'sure'
    if "amounts" not in st.session_state:
        # filled when problem starts
        st.session_state.amounts = None
    if "phase1_choices" not in st.session_state:
        st.session_state.phase1_choices = []
    if "results" not in st.session_state:
        st.session_state.results = []  # list of dict rows
    if "__violation_msg" not in st.session_state:
        st.session_state["__violation_msg"] = None


init_state()


# ---------- Intro / Start ----------
if not st.session_state.started:
    st.write(
        "This survey examines how people make decisions involving **risk**. "
        "You'll see a series of problems where you choose between a risky **gamble** and a **sure amount**. "
        "Each problem has **two phases**: a broad first pass across 7 amounts, then a refined pass that zooms in."
    )
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.name = st.text_input("Your name *", value=st.session_state.name)
    with col2:
        st.session_state.age = st.number_input("Age *", min_value=18, max_value=120, value=18, step=1)

    if st.button("Start Survey", type="primary", use_container_width=True):
        st.session_state.started = True
        # Set up first problem
        st.session_state.index = 0
        st.session_state.phase = 1
        st.session_state.current_choices = [None] * 7
        st.session_state.phase1_choices = []
        st.session_state.results = []

        prospect = st.session_state.prospects[st.session_state.index]
        st.session_state.amounts = generate_sure_amounts(prospect, phase=1)
        st.rerun()
    st.stop()


# ---------- Show any violation message (from last callback) ----------
if st.session_state.get("__violation_msg"):
    st.error(st.session_state["__violation_msg"])
    st.session_state["__violation_msg"] = None


# ---------- Main Flow ----------
total = len(st.session_state.prospects)
current = st.session_state.index + 1
st.progress((st.session_state.index) / total)

prospect = st.session_state.prospects[st.session_state.index]
ev = expected_value(prospect)
domain = "Gain Domain" if max(prospect["outcomes"]) > 0 else "Loss Domain"

st.subheader(f"Problem {current} of {total} — Phase {st.session_state.phase}")
st.caption(domain)
st.markdown(f"**Gamble:** {describe_prospect(prospect)}")
st.markdown(f"**Expected Value:** {format_money(ev)}")

# Instruction box
if domain.startswith("Gain"):
    st.info("For each row below, choose whether you prefer to **RECEIVE** the sure amount or **take the gamble**.")
else:
    st.info("For each row below, choose whether you prefer to **PAY** the sure amount to avoid the gamble, or **take the gamble**.")

# Ensure amounts exist for this phase
amounts = st.session_state.amounts
choices = st.session_state.current_choices

# ---------- Radio Callback ----------
def _on_radio_change(key: str, idx: int):
    val = st.session_state.get(key)
    if val is None:
        return
    proposed = "prospect" if val == "Prefer Gamble" else "sure"
    violated, msg = check_monotonic_violation(choices, amounts, proposed, idx)
    if violated:
        # Reset this selection; show message on next render
        st.session_state[key] = None
        st.session_state.current_choices[idx] = None
        st.session_state["__violation_msg"] = msg
    else:
        st.session_state.current_choices[idx] = proposed


# ---------- Render 7 rows (no forms; live on_change) ----------
for i, amt in enumerate(amounts):
    c1, c2 = st.columns([3, 4])
    with c1:
        st.markdown(f"**Sure amount:** {format_money(amt)}")
    with c2:
        key = f"choice_{current}_{st.session_state.phase}_{i}"
        default_index = 0 if choices[i] == "prospect" else (1 if choices[i] == "sure" else None)
        st.radio(
            "Your choice",
            options=("Prefer Gamble", f"Prefer Sure {format_money(amt)}"),
            index=default_index,
            horizontal=True,
            key=key,
            on_change=_on_radio_change,
            args=(key, i),
        )

# ---------- Continue Button ----------
if st.button("Continue", type="primary", use_container_width=True):
    # Require all rows answered
    if any(c is None for c in choices):
        st.error("Please answer **all 7 rows** before continuing.")
        st.stop()

    # Guard (should be consistent due to live check)
    err = check_consistency(choices, amounts)
    if err:
        st.error(err)
        st.stop()

    if st.session_state.phase == 1:
        # Save phase1 choices & set up phase 2
        st.session_state.phase1_choices.append(list(choices))
        st.session_state.phase = 2
        st.session_state.current_choices = [None] * 7
        st.session_state.amounts = generate_sure_amounts(
            prospect, phase=2, phase1_choices=choices
        )
        st.rerun()
    else:
        # Phase 2 complete -> compute CE & store result
        ce = compute_certainty_equivalent(choices, amounts)
        risk_att = risk_attitude_from_ce(ce, ev)

        st.session_state.results.append({
            "participant": st.session_state.name,
            "age": st.session_state.age,
            "problem_index": st.session_state.index + 1,
            "prospect": describe_prospect(prospect),
            "expected_value": round(ev, 2),
            "certainty_equivalent": ce,
            "domain": "Gain" if domain.startswith("Gain") else "Loss",
            "risk_attitude": risk_att,
        })

        # Advance to next problem
        st.session_state.index += 1
        st.session_state.phase = 1
        st.session_state.current_choices = [None] * 7
        if st.session_state.index < total:
            next_prospect = st.session_state.prospects[st.session_state.index]
            st.session_state.amounts = generate_sure_amounts(next_prospect, phase=1)
            st.rerun()

# ---------- If finished ----------
if st.session_state.index >= total:
    st.success("Survey complete — thanks!")

    if st.session_state.results:
        df = pd.DataFrame(st.session_state.results)
        st.dataframe(df, hide_index=True, use_container_width=True)

        # JSON download
        json_data = json.dumps(st.session_state.results, indent=2)
        st.download_button(
            "Download JSON",
            data=json_data,
            file_name="risk_survey_results.json",
            mime="application/json",
        )

        # CSV download
        csv_data = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download CSV",
            data=csv_data,
            file_name="risk_survey_results.csv",
            mime="text/csv",
        )
    st.stop()
