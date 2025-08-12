
import random
import json
import io
from datetime import datetime

import streamlit as st
import pandas as pd

# ---------- Page setup ----------
st.set_page_config(page_title="Risk Preference Survey", layout="wide")

# ---------- Helper data ----------

# Prospects adapted from your HTML (gains and losses)
GAINS = [
    {"outcomes": [0, 50], "probabilities": [0.99, 0.01], "description": "1% chance to win $50, 99% chance to win nothing"},
    {"outcomes": [0, 50], "probabilities": [0.95, 0.05], "description": "5% chance to win $50, 95% chance to win nothing"},
    {"outcomes": [0, 50], "probabilities": [0.90, 0.10], "description": "10% chance to win $50, 90% chance to win nothing"},
    {"outcomes": [0, 50], "probabilities": [0.75, 0.25], "description": "25% chance to win $50, 75% chance to win nothing"},
    {"outcomes": [0, 50], "probabilities": [0.50, 0.50], "description": "50% chance to win $50, 50% chance to win nothing"},

    {"outcomes": [0, 100], "probabilities": [0.95, 0.05], "description": "5% chance to win $100, 95% chance to win nothing"},
    {"outcomes": [0, 100], "probabilities": [0.90, 0.10], "description": "10% chance to win $100, 90% chance to win nothing"},
    {"outcomes": [0, 100], "probabilities": [0.75, 0.25], "description": "25% chance to win $100, 75% chance to win nothing"},
    {"outcomes": [0, 100], "probabilities": [0.50, 0.50], "description": "50% chance to win $100, 50% chance to win nothing"},
    {"outcomes": [0, 100], "probabilities": [0.25, 0.75], "description": "75% chance to win $100, 25% chance to win nothing"},
    {"outcomes": [0, 100], "probabilities": [0.10, 0.90], "description": "90% chance to win $100, 10% chance to win nothing"},
    {"outcomes": [0, 100], "probabilities": [0.05, 0.95], "description": "95% chance to win $100, 5% chance to win nothing"},
    {"outcomes": [0, 100], "probabilities": [0.01, 0.99], "description": "99% chance to win $100, 1% chance to win nothing"},

    {"outcomes": [0, 200], "probabilities": [0.99, 0.01], "description": "1% chance to win $200, 99% chance to win nothing"},
    {"outcomes": [0, 200], "probabilities": [0.95, 0.05], "description": "5% chance to win $200, 95% chance to win nothing"},
    {"outcomes": [0, 200], "probabilities": [0.90, 0.10], "description": "10% chance to win $200, 90% chance to win nothing"},
    {"outcomes": [0, 200], "probabilities": [0.50, 0.50], "description": "50% chance to win $200, 50% chance to win nothing"},
    {"outcomes": [0, 200], "probabilities": [0.25, 0.75], "description": "75% chance to win $200, 25% chance to win nothing"},
    {"outcomes": [0, 200], "probabilities": [0.10, 0.90], "description": "90% chance to win $200, 10% chance to win nothing"},
    {"outcomes": [0, 200], "probabilities": [0.05, 0.95], "description": "95% chance to win $200, 5% chance to win nothing"},
    {"outcomes": [0, 200], "probabilities": [0.01, 0.99], "description": "99% chance to win $200, 1% chance to win nothing"},

    {"outcomes": [0, 400], "probabilities": [0.99, 0.01], "description": "1% chance to win $400, 99% chance to win nothing"},
    {"outcomes": [0, 400], "probabilities": [0.95, 0.05], "description": "5% chance to win $400, 95% chance to win nothing"},
    {"outcomes": [0, 400], "probabilities": [0.01, 0.99], "description": "99% chance to win $400, 1% chance to win nothing"},

    {"outcomes": [50, 100], "probabilities": [0.90, 0.10], "description": "10% chance to win $100, 90% chance to win $50"},
    {"outcomes": [50, 100], "probabilities": [0.50, 0.50], "description": "50% chance to win $100, 50% chance to win $50"},
    {"outcomes": [50, 100], "probabilities": [0.25, 0.75], "description": "75% chance to win $100, 25% chance to win $50"},

    {"outcomes": [50, 150], "probabilities": [0.95, 0.05], "description": "5% chance to win $150, 95% chance to win $50"},
    {"outcomes": [50, 150], "probabilities": [0.90, 0.10], "description": "10% chance to win $150, 90% chance to win $50"},
    {"outcomes": [50, 150], "probabilities": [0.50, 0.50], "description": "50% chance to win $150, 50% chance to win $50"},
    {"outcomes": [50, 150], "probabilities": [0.25, 0.75], "description": "75% chance to win $150, 25% chance to win $50"},
    {"outcomes": [50, 150], "probabilities": [0.10, 0.90], "description": "90% chance to win $150, 10% chance to win $50"},
    {"outcomes": [50, 150], "probabilities": [0.05, 0.95], "description": "95% chance to win $150, 5% chance to win $50"},

    {"outcomes": [100, 200], "probabilities": [0.95, 0.05], "description": "5% chance to win $200, 95% chance to win $100"},
    {"outcomes": [100, 200], "probabilities": [0.90, 0.10], "description": "10% chance to win $200, 90% chance to win $100"},
    {"outcomes": [100, 200], "probabilities": [0.50, 0.50], "description": "50% chance to win $200, 50% chance to win $100"},
    {"outcomes": [100, 200], "probabilities": [0.25, 0.75], "description": "75% chance to win $200, 25% chance to win $100"},
    {"outcomes": [100, 200], "probabilities": [0.10, 0.90], "description": "90% chance to win $200, 10% chance to win $100"},
]

LOSSES = [
    {"outcomes": [0, -50], "probabilities": [0.90, 0.10], "description": "10% chance to lose $50, 90% chance to lose nothing"},
    {"outcomes": [0, -50], "probabilities": [0.50, 0.50], "description": "50% chance to lose $50, 50% chance to lose nothing"},
    {"outcomes": [0, -50], "probabilities": [0.10, 0.90], "description": "90% chance to lose $50, 10% chance to lose nothing"},

    {"outcomes": [0, -100], "probabilities": [0.95, 0.05], "description": "5% chance to lose $100, 95% chance to lose nothing"},
    {"outcomes": [0, -100], "probabilities": [0.75, 0.25], "description": "25% chance to lose $100, 75% chance to lose nothing"},
    {"outcomes": [0, -100], "probabilities": [0.50, 0.50], "description": "50% chance to lose $100, 50% chance to lose nothing"},
    {"outcomes": [0, -100], "probabilities": [0.25, 0.75], "description": "75% chance to lose $100, 25% chance to lose nothing"},
    {"outcomes": [0, -100], "probabilities": [0.05, 0.95], "description": "95% chance to lose $100, 5% chance to lose nothing"},

    {"outcomes": [0, -200], "probabilities": [0.99, 0.01], "description": "1% chance to lose $200, 99% chance to lose nothing"},
    {"outcomes": [0, -200], "probabilities": [0.95, 0.05], "description": "5% chance to lose $200, 95% chance to lose nothing"},
    {"outcomes": [0, -200], "probabilities": [0.50, 0.50], "description": "50% chance to lose $200, 50% chance to lose nothing"},
    {"outcomes": [0, -200], "probabilities": [0.10, 0.90], "description": "90% chance to lose $200, 10% chance to lose nothing"},
    {"outcomes": [0, -200], "probabilities": [0.05, 0.95], "description": "95% chance to lose $200, 5% chance to lose nothing"},

    {"outcomes": [0, -400], "probabilities": [0.99, 0.01], "description": "1% chance to lose $400, 99% chance to lose nothing"},
    {"outcomes": [0, -400], "probabilities": [0.95, 0.05], "description": "5% chance to lose $400, 95% chance to lose nothing"},
    {"outcomes": [0, -400], "probabilities": [0.01, 0.99], "description": "99% chance to lose $400, 1% chance to lose nothing"},

    {"outcomes": [-50, -100], "probabilities": [0.50, 0.50], "description": "50% chance to lose $100, 50% chance to lose $50"},
    {"outcomes": [-50, -100], "probabilities": [0.25, 0.75], "description": "75% chance to lose $100, 25% chance to lose $50"},
    {"outcomes": [-50, -100], "probabilities": [0.10, 0.90], "description": "90% chance to lose $100, 10% chance to lose $50"},

    {"outcomes": [-50, -150], "probabilities": [0.95, 0.05], "description": "5% chance to lose $150, 95% chance to lose $50"},
    {"outcomes": [-50, -150], "probabilities": [0.90, 0.10], "description": "10% chance to lose $150, 90% chance to lose $50"},
    {"outcomes": [-50, -150], "probabilities": [0.50, 0.50], "description": "50% chance to lose $150, 50% chance to lose $50"},
    {"outcomes": [-50, -150], "probabilities": [0.25, 0.75], "description": "75% chance to lose $150, 25% chance to lose $50"},
    {"outcomes": [-50, -150], "probabilities": [0.10, 0.90], "description": "90% chance to lose $150, 10% chance to lose $50"},
    {"outcomes": [-50, -150], "probabilities": [0.05, 0.95], "description": "95% chance to lose $150, 5% chance to lose $50"},

    {"outcomes": [-100, -200], "probabilities": [0.95, 0.05], "description": "5% chance to lose $200, 95% chance to lose $100"},
    {"outcomes": [-100, -200], "probabilities": [0.90, 0.10], "description": "10% chance to lose $200, 90% chance to lose $100"},
    {"outcomes": [-100, -200], "probabilities": [0.50, 0.50], "description": "50% chance to lose $200, 50% chance to lose $100"},
    {"outcomes": [-100, -200], "probabilities": [0.25, 0.75], "description": "75% chance to lose $200, 25% chance to lose $100"},
    {"outcomes": [-100, -200], "probabilities": [0.10, 0.90], "description": "90% chance to lose $200, 10% chance to lose $100"},
]

# ---------- Utilities ----------

def expected_value(prospect):
    return sum(o * p for o, p in zip(prospect["outcomes"], prospect["probabilities"]))

def is_loss_domain(prospect):
    return any(o < 0 for o in prospect["outcomes"])

def generate_sure_amounts(prospect, phase, phase1_choices=None):
    """Generate 7 sure amounts.
    Phase 1: logarithmically spaced (descending).
    Phase 2: linearly spaced between adjusted bounds based on phase 1 choices.
    """
    lo, hi = min(prospect["outcomes"]), max(prospect["outcomes"])
    rng = hi - lo

    if phase == 1:
        # Log-like spacing: we want 7 descending amounts between hi and lo
        # We'll create a smooth spread emphasizing the extremes
        amounts = []
        # Use geometric-like spacing over positive range; handle negatives by shifting
        shift = 0
        if lo <= 0:
            shift = -lo + 1  # ensure positivity
        adj_lo, adj_hi = lo + shift, hi + shift
        for i in range(7):
            # t from 0..1; place points from hi down to lo
            t = i / 6
            val = adj_hi * (1 - t**1.5) + adj_lo * (t**1.5)  # non-linear blend
            amounts.append(round((val - shift), 2))
        # Ensure strict descending (largest to smallest)
        amounts = sorted(amounts, reverse=True)
        return amounts

    # Phase 2
    if not phase1_choices:
        # Fallback to a simple linear spread if phase1 choices missing
        return [round(hi - i*(rng/6), 2) for i in range(7)]

    # Determine lowest accepted (sure) and highest rejected (prospect) from phase 1
    phase1_amounts = generate_sure_amounts(prospect, 1)
    lowest_accepted = None
    highest_rejected = None
    for amt, choice in zip(phase1_amounts, phase1_choices):
        if choice == "sure":
            if lowest_accepted is None or amt < lowest_accepted:
                lowest_accepted = amt
        elif choice == "prospect":
            if highest_rejected is None or amt > highest_rejected:
                highest_rejected = amt

    # Compute bounds (similar to your HTML logic)
    if lowest_accepted is not None and highest_rejected is not None:
        lower = lowest_accepted - abs(lowest_accepted) * 0.25
        upper = highest_rejected + abs(highest_rejected) * 0.25
    elif lowest_accepted is not None:
        lower = lowest_accepted - abs(lowest_accepted) * 0.5
        upper = lowest_accepted + abs(lowest_accepted) * 0.25
    elif highest_rejected is not None:
        lower = highest_rejected - abs(highest_rejected) * 0.25
        upper = highest_rejected + abs(highest_rejected) * 0.5
    else:
        lower, upper = lo, hi

    lo2, hi2 = min(lower, upper), max(lower, upper)
    # 7 linearly spaced amounts descending
    amounts = [round(hi2 - i * (hi2 - lo2) / 6, 2) for i in range(7)]
    return amounts

def check_consistency(choices, amounts):
    """Return None if consistent; otherwise an error string.
    Rule: If you prefer a sure amount at some row, you should prefer sure for all *higher* amounts.
          If you prefer the prospect at some row, you should prefer prospect for all *lower* amounts.
    Here, amounts are descending (highest first).
    """
    # Find first index where choice is made; scan for violations.
    n = len(choices)
    for i in range(n):
        if choices[i] is None:
            continue
        if choices[i] == "sure":
            # No earlier "prospect" allowed at any j < i (since those are higher amounts)
            for j in range(i):
                if choices[j] == "prospect":
                    return f"Inconsistency: You chose 'Prefer Sure ${amounts[i]}' but earlier rejected a higher sure amount (${amounts[j]})."
        elif choices[i] == "prospect":
            # No later "sure" allowed at any j > i (since those are lower amounts)
            for j in range(i+1, n):
                if choices[j] == "sure":
                    return f"Inconsistency: You chose 'Prefer Gamble' over ${amounts[i]} but later accepted a lower sure amount (${amounts[j]})."
    return None

def compute_certainty_equivalent(choices, amounts):
    """Given 7 choices and corresponding amounts (descending), compute CE as midpoint
    between highest rejected and lowest accepted when both exist; otherwise pick the chosen one.
    """
    lowest_accepted = None
    highest_rejected = None
    for amt, ch in zip(amounts, choices):
        if ch == "sure":
            lowest_accepted = amt  # amounts are descending, so last 'sure' encountered is the lowest accepted
        elif ch == "prospect" and lowest_accepted is None:
            # first block of 'prospect' before any 'sure' captures highest rejected
            if highest_rejected is None or amt > highest_rejected:
                highest_rejected = amt

    if lowest_accepted is not None and highest_rejected is not None:
        return round((lowest_accepted + highest_rejected) / 2, 2)
    if lowest_accepted is not None:
        return round(lowest_accepted, 2)
    if highest_rejected is not None:
        return round(highest_rejected, 2)
    return 0.0

def export_json_blob(data_dict):
    buf = io.BytesIO()
    buf.write(json.dumps(data_dict, indent=2).encode("utf-8"))
    buf.seek(0)
    return buf

def export_csv_blob(results, name, age):
    # Flatten to rows
    rows = []
    for i, r in enumerate(results, start=1):
        rows.append({
            "Name": name,
            "Age": age,
            "Problem": i,
            "Domain": r["domain"],
            "Prospect": r["prospect"],
            "Expected_Value": r["expected_value"],
            "Certainty_Equivalent": r["certainty_equivalent"],
            "Risk_Attitude": r["risk_attitude"],
        })
    df = pd.DataFrame(rows)
    return df.to_csv(index=False).encode("utf-8")

# ---------- Session State init ----------
if "started" not in st.session_state:
    st.session_state.started = False
if "name" not in st.session_state:
    st.session_state.name = ""
if "age" not in st.session_state:
    st.session_state.age = None
if "prospects" not in st.session_state:
    st.session_state.prospects = []
if "index" not in st.session_state:
    st.session_state.index = 0
if "phase" not in st.session_state:
    st.session_state.phase = 1  # 1 or 2
if "phase1_choices" not in st.session_state:
    st.session_state.phase1_choices = []  # stores choices for each prospect (list of 7)
if "current_choices" not in st.session_state:
    st.session_state.current_choices = [None] * 7
if "amounts" not in st.session_state:
    st.session_state.amounts = []
if "results" not in st.session_state:
    st.session_state.results = []

# ---------- UI ----------
st.title("Risk Preference Survey")

if not st.session_state.started:
    with st.expander("What is this?", expanded=True):
        st.markdown(
            """
            This survey examines how people make decisions involving **risk**. 
            You'll see a series of problems where you choose between a **risky gamble** 
            and a **sure amount**. Each problem has **two phases**:
            1) an initial pass across 7 sure amounts, and 
            2) a refined pass that zooms in based on your first answers.
            """
        )

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.name = st.text_input("Your name *", value=st.session_state.name).strip()
    with col2:
        st.session_state.age = st.number_input("Age *", min_value=18, max_value=120, step=1, value=st.session_state.age or 18)

    if st.button("Start Survey", type="primary", use_container_width=True):
        if not st.session_state.name or st.session_state.age is None:
            st.warning("Please enter both name and age.")
            st.stop()

        # Randomly select 5 gains + 5 losses, shuffle
        gains = random.sample(GAINS, 5)
        losses = random.sample(LOSSES, 5)
        prospects = gains + losses
        random.shuffle(prospects)

        st.session_state.prospects = prospects
        st.session_state.index = 0
        st.session_state.phase = 1
        st.session_state.phase1_choices = []  # reset all
        st.session_state.current_choices = [None] * 7
        st.session_state.results = []

        # Precompute first set of amounts
        st.session_state.amounts = generate_sure_amounts(st.session_state.prospects[0], phase=1)
        st.session_state.started = True
        st.rerun()

else:
    # Survey in progress or finished
    total_problems = len(st.session_state.prospects)
    current = st.session_state.index

    # Progress
    total_steps = total_problems * 2  # two phases each
    current_step = current * 2 + (st.session_state.phase - 1)
    st.progress(min(1.0, current_step / total_steps))

    if current >= total_problems:
        # Done
        st.success("Survey complete!")
        # Show results table
        df = pd.DataFrame(st.session_state.results)
        st.dataframe(df, use_container_width=True)

        # Export buttons
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
        summary = {
            "participant": {"name": st.session_state.name, "age": st.session_state.age, "timestamp_utc": timestamp},
            "results": st.session_state.results,
            "summary": {
                "totalProblems": len(st.session_state.results),
                "gainProblems": sum(1 for r in st.session_state.results if r["domain"] == "Gain Domain"),
                "lossProblems": sum(1 for r in st.session_state.results if r["domain"] == "Loss Domain"),
                "riskAverseCount": sum(1 for r in st.session_state.results if r["risk_attitude"] == "Risk Averse"),
                "riskSeekingCount": sum(1 for r in st.session_state.results if r["risk_attitude"] == "Risk Seeking"),
                "riskNeutralCount": sum(1 for r in st.session_state.results if r["risk_attitude"] == "Risk Neutral"),
            }
        }

        st.download_button(
            "Download results (JSON)",
            data=export_json_blob(summary),
            file_name=f"risk_survey_{st.session_state.name.replace(' ', '_')}_{timestamp}.json",
            mime="application/json",
            use_container_width=True,
        )

        st.download_button(
            "Download results (CSV)",
            data=export_csv_blob(st.session_state.results, st.session_state.name, st.session_state.age),
            file_name=f"risk_survey_{st.session_state.name.replace(' ', '_')}_{timestamp}.csv",
            mime="text/csv",
            use_container_width=True,
        )

        # Restart option
        if st.button("Start a new survey", use_container_width=True):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

    else:
        # Show current problem
        prospect = st.session_state.prospects[current]
        ev = expected_value(prospect)
        domain = "Loss Domain" if is_loss_domain(prospect) else "Gain Domain"

        st.subheader(f"Problem {current + 1} of {total_problems} — Phase {st.session_state.phase}")
        st.caption(domain)
        st.markdown(f"**Gamble:** {prospect['description']}")
        st.markdown(f"**Expected Value:** ${ev:.2f}")

        # Prompt text
        if domain == "Loss Domain":
            st.info("For each row below, choose whether you prefer to **PAY** the sure amount to avoid the gamble, or **take the gamble**.")
        else:
            st.info("For each row below, choose whether you prefer to **RECEIVE** the sure amount or **take the gamble**.")

        # Amounts for this phase
        amounts = st.session_state.amounts
        choices = st.session_state.current_choices

        # Render 7 rows with radios
        # Determine forced regions based on current selections to enforce monotonicity:
        # - If a higher sure amount is accepted, all higher rows (above that index) are forced to 'sure'.
        # - If a lower sure amount is rejected in favor of the gamble, all lower rows (below that index) are forced to 'prospect'.
        first_sure_idx = None
        last_prospect_idx = None
        for _i, ch in enumerate(choices):
            if ch == "sure" and first_sure_idx is None:
                first_sure_idx = _i
            if ch == "prospect":
                last_prospect_idx = _i if last_prospect_idx is None else max(last_prospect_idx, _i)

        # Live monotonic enforcement (no form): selecting a radio triggers a rerun and locks appropriate rows.
        # Helpers for radio on_change
        def _set_choice(key, idx):
            val = st.session_state.get(key)
            if val is None:
                return
            st.session_state.current_choices[idx] = "prospect" if val == "Prefer Gamble" else "sure"

        # Determine forced regions based on current selections
        choices = st.session_state.current_choices
        first_sure_idx = None
        last_prospect_idx = None
        for _i, ch in enumerate(choices):
            if ch == "sure" and first_sure_idx is None:
                first_sure_idx = _i
            if ch == "prospect":
                last_prospect_idx = _i if last_prospect_idx is None else max(last_prospect_idx, _i)

        for i, amt in enumerate(amounts):
            col_a, col_b = st.columns([3, 3])
            with col_a:
                st.markdown(f"**Sure amount:** ${amt}")
            with col_b:
                force_choice = None
                if first_sure_idx is not None and i < first_sure_idx:
                    force_choice = "sure"
                elif last_prospect_idx is not None and i > last_prospect_idx:
                    force_choice = "prospect"

                options = ("Prefer Gamble", f"Prefer Sure ${amt}")
                key = f"choice_{current}_{st.session_state.phase}_{i}"

                if force_choice is not None:
                    # Force and disable
                    st.session_state.current_choices[i] = force_choice
                    default_index = 0 if force_choice == "prospect" else 1
                    st.radio(
                        "Your choice",
                        options=options,
                        index=default_index,
                        horizontal=True,
                        key=key,
                        disabled=True,
                    )
                else:
                    # Free selection; default from current state
                    default_index = None
                    if st.session_state.current_choices[i] is not None:
                        default_index = 0 if st.session_state.current_choices[i] == "prospect" else 1
                    st.radio(
                        "Your choice",
                        options=options,
                        index=default_index,
                        horizontal=True,
                        key=key,
                        on_change=_set_choice,
                        args=(key, i),
                    )

        # Continue button to advance phase or problem
        if st.button("Continue", use_container_width=True):
            choices = st.session_state.current_choices

            # Re-enforce monotonic pattern before validating
            first_sure_idx = None
            last_prospect_idx = None
            for _i, ch in enumerate(choices):
                if ch == "sure" and first_sure_idx is None:
                    first_sure_idx = _i
                if ch == "prospect":
                    last_prospect_idx = _i if last_prospect_idx is None else max(last_prospect_idx, _i)

            for i in range(len(choices)):
                if first_sure_idx is not None and i < first_sure_idx:
                    choices[i] = "sure"
                if last_prospect_idx is not None and i > last_prospect_idx:
                    choices[i] = "prospect"

            # Validate all selected
            if any(c is None for c in choices):
                st.error("Please make a selection for all 7 rows.")
                st.stop()

            # Consistency guard
            err = check_consistency(choices, amounts)
            if err:
                st.error(err)
                st.stop()

            # Proceed
            if st.session_state.phase == 1:
                st.session_state.phase1_choices.append(list(choices))
                st.session_state.phase = 2
                st.session_state.amounts = generate_sure_amounts(
                    prospect, phase=2, phase1_choices=choices
                )
                st.session_state.current_choices = [None] * 7
                st.rerun()
            else:
                ce = compute_certainty_equivalent(choices, amounts)
                risk_att = (
                    "Risk Averse" if ce < ev else
                    "Risk Seeking" if ce > ev else
                    "Risk Neutral"
                )
                st.session_state.results.append({
                    "prospect": prospect["description"],
                    "expected_value": round(ev, 2),
                    "certainty_equivalent": ce,
                    "domain": domain,
                    "risk_attitude": risk_att,
                })

                st.session_state.index += 1
                st.session_state.phase = 1
                st.session_state.current_choices = [None] * 7

                if st.session_state.index < total_problems:
                    st.session_state.amounts = generate_sure_amounts(
                        st.session_state.prospects[st.session_state.index], phase=1
                    )
                st.rerun()
