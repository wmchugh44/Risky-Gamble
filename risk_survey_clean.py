import random
import json
import io
from datetime import datetime

import streamlit as st
import pandas as pd

# ---------- Page setup ----------
st.set_page_config(page_title="Risk Preference Survey", layout="wide")

# ---------- Helper data ----------
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

def describe_prospect(prospect):
    """Return a clear human-readable description of the gamble."""
    outcomes = prospect["outcomes"]
    probabilities = prospect["probabilities"]
    
    if len(outcomes) == 2 and len(probabilities) == 2:
        o1, o2 = outcomes
        p1, p2 = probabilities
        
        def format_outcome(x):
            if x == 0:
                return "nothing"
            elif x > 0:
                return f"win ${x:,.0f}"
            else:
                return f"lose ${abs(x):,.0f}"
        
        return f"{int(p2*100)}% chance to {format_outcome(o2)}, {int(p1*100)}% chance to {format_outcome(o1)}"
    
    return prospect.get("description", "")

def check_monotonic_violation(choices, amounts, new_choice, idx):
    """
    Check if a new choice would violate monotonicity.
    amounts is descending (largest first).
    Returns (violation: bool, message: str)
    """
    temp = list(choices)
    temp[idx] = new_choice
    
    for i, ch in enumerate(temp):
        if ch is None:
            continue
        
        if ch == "prospect":
            # If prefer gamble at i, must prefer it at all j > i (smaller amounts)
            for j in range(i + 1, len(temp)):
                if temp[j] == "sure":
                    msg = (
                        f"**Monotonicity violation detected.**\n\n"
                        f"If you prefer the gamble over ${amounts[i]:,.2f}, you must also "
                        f"prefer it over any smaller amount like ${amounts[j]:,.2f}.\n\n"
                        f"Please reconsider your choice."
                    )
                    return True, msg
        
        elif ch == "sure":
            # If prefer sure at i, must prefer sure at all j < i (larger amounts)
            for j in range(i):
                if temp[j] == "prospect":
                    msg = (
                        f"**Monotonicity violation detected.**\n\n"
                        f"If you prefer ${amounts[i]:,.2f} over the gamble, you must also "
                        f"prefer any larger amount like ${amounts[j]:,.2f}.\n\n"
                        f"Please reconsider your choice."
                    )
                    return True, msg
    
    return False, ""

def expected_value(prospect):
    """Calculate expected value of a prospect."""
    return sum(o * p for o, p in zip(prospect["outcomes"], prospect["probabilities"]))

def is_loss_domain(prospect):
    """Check if prospect is in loss domain."""
    return any(o < 0 for o in prospect["outcomes"])

def generate_sure_amounts(prospect, phase, phase1_choices=None):
    """Generate 7 sure amounts for the given phase."""
    outcomes = prospect["outcomes"]
    lo, hi = min(outcomes), max(outcomes)
    
    if phase == 1:
        # Phase 1: Non-linear spacing emphasizing extremes
        amounts = []
        shift = max(0, -lo + 1) if lo <= 0 else 0
        adj_lo, adj_hi = lo + shift, hi + shift
        
        for i in range(7):
            t = i / 6
            val = adj_hi * (1 - t**1.5) + adj_lo * (t**1.5)
            amounts.append(round(val - shift, 2))
        
        amounts.sort(reverse=True)  # Ensure descending
        return amounts
    
    # Phase 2: Linear spacing based on phase 1 choices
    if not phase1_choices:
        rng = hi - lo
        return [round(hi - i * (rng / 6), 2) for i in range(7)]
    
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
    
    # Determine bounds
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
    amounts = [round(hi2 - i * (hi2 - lo2) / 6, 2) for i in range(7)]
    return amounts

def compute_certainty_equivalent(choices, amounts):
    """Compute certainty equivalent from choices."""
    lowest_accepted = None
    highest_rejected = None
    
    for amt, choice in zip(amounts, choices):
        if choice == "sure":
            lowest_accepted = amt
        elif choice == "prospect" and lowest_accepted is None:
            if highest_rejected is None or amt > highest_rejected:
                highest_rejected = amt
    
    if lowest_accepted is not None and highest_rejected is not None:
        return round((lowest_accepted + highest_rejected) / 2, 2)
    elif lowest_accepted is not None:
        return round(lowest_accepted, 2)
    elif highest_rejected is not None:
        return round(highest_rejected, 2)
    else:
        return 0.0

def export_json_blob(data_dict):
    """Export data as JSON blob."""
    buf = io.BytesIO()
    buf.write(json.dumps(data_dict, indent=2).encode("utf-8"))
    buf.seek(0)
    return buf

def export_csv_blob(results, name, age):
    """Export results as CSV blob."""
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
    st.session_state.phase = 1
if "phase1_choices" not in st.session_state:
    st.session_state.phase1_choices = []
if "current_choices" not in st.session_state:
    st.session_state.current_choices = [None] * 7
if "amounts" not in st.session_state:
    st.session_state.amounts = []
if "results" not in st.session_state:
    st.session_state.results = []
if "__violation_msg" not in st.session_state:
    st.session_state.__violation_msg = None

# ---------- Display violation message if exists ----------
if st.session_state.__violation_msg:
    st.error(st.session_state.__violation_msg)
    st.session_state.__violation_msg = None

# ---------- UI ----------
st.title("Risk Preference Survey")

if not st.session_state.started:
    with st.expander("What is this?", expanded=True):
        st.markdown(
            """
            This survey examines how people make decisions involving **risk**. 
            You'll see a series of problems where you choose between a **risky gamble** 
            and a **sure amount**. Each problem has **two phases**:
            
            1. An initial pass across 7 sure amounts
            2. A refined pass that zooms in based on your first answers
            
            The survey is based on research by Tversky & Kahneman (1992).
            """
        )

    col1, col2 = st.columns(2)
    with col1:
        st.session_state.name = st.text_input("Your name *", value=st.session_state.name).strip()
    with col2:
        st.session_state.age = st.number_input("Age *", min_value=18, max_value=120, step=1, 
                                             value=st.session_state.age or 18)

    if st.button("Start Survey", type="primary", use_container_width=True):
        if not st.session_state.name or st.session_state.age is None:
            st.warning("Please enter both name and age.")
            st.stop()

        # Initialize survey
        gains = random.sample(GAINS, 5)
        losses = random.sample(LOSSES, 5)
        prospects = gains + losses
        random.shuffle(prospects)

        st.session_state.prospects = prospects
        st.session_state.index = 0
        st.session_state.phase = 1
        st.session_state.phase1_choices = []
        st.session_state.current_choices = [None] * 7
        st.session_state.results = []
        st.session_state.amounts = generate_sure_amounts(prospects[0], phase=1)
        st.session_state.started = True
        st.rerun()

else:
    # Survey in progress or finished
    total_problems = len(st.session_state.prospects)
    current = st.session_state.index

    # Progress bar
    total_steps = total_problems * 2
    current_step = current * 2 + (st.session_state.phase - 1)
    st.progress(min(1.0, current_step / total_steps))

    if current >= total_problems:
        # Survey complete
        st.success("Survey complete! 🎉")
        
        # Display results
        df = pd.DataFrame(st.session_state.results)
        st.dataframe(df, use_container_width=True)

        # Export options
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
        summary = {
            "participant": {
                "name": st.session_state.name,
                "age": st.session_state.age,
                "timestamp_utc": timestamp
            },
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

        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "Download results (JSON)",
                data=export_json_blob(summary),
                file_name=f"risk_survey_{st.session_state.name.replace(' ', '_')}_{timestamp}.json",
                mime="application/json",
                use_container_width=True,
            )
        
        with col2:
            st.download_button(
                "Download results (CSV)",
                data=export_csv_blob(st.session_state.results, st.session_state.name, st.session_state.age),
                file_name=f"risk_survey_{st.session_state.name.replace(' ', '_')}_{timestamp}.csv",
                mime="text/csv",
                use_container_width=True,
            )

        if st.button("Start a new survey", use_container_width=True):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

    else:
        # Current problem - only render if started and amounts exist
        if st.session_state.started and st.session_state.amounts:
            prospect = st.session_state.prospects[current]
            ev = expected_value(prospect)
            domain = "Loss Domain" if is_loss_domain(prospect) else "Gain Domain"

            st.subheader(f"Problem {current + 1} of {total_problems} — Phase {st.session_state.phase}")
            st.caption(domain)
            
            st.markdown(f"**Gamble:** {describe_prospect(prospect)}")
            st.markdown(f"**Expected Value:** ${ev:.2f}")

            # Instructions
            if domain == "Loss Domain":
                st.info("For each row below, choose whether you prefer to **PAY** the sure amount to avoid the gamble, or **take the gamble**.")
            else:
                st.info("For each row below, choose whether you prefer to **RECEIVE** the sure amount or **take the gamble**.")

            # Radio choice callback function
            def on_radio_change(key, idx):
                val = st.session_state.get(key)
                if val is None:
                    return
                
                proposed = "prospect" if val == "Prefer Gamble" else "sure"
                violated, msg = check_monotonic_violation(
                    st.session_state.current_choices, 
                    st.session_state.amounts, 
                    proposed, 
                    idx
                )
                
                if violated:
                    st.session_state.__violation_msg = msg
                    st.session_state[key] = None
                    st.session_state.current_choices[idx] = None
                else:
                    st.session_state.current_choices[idx] = proposed

            # Render choice rows
            amounts = st.session_state.amounts
            choices = st.session_state.current_choices
            
            for i, amt in enumerate(amounts):
                col_a, col_b = st.columns([3, 4])
                with col_a:
                    st.markdown(f"**Sure amount:** ${amt:,.2f}")
                with col_b:
                    options = ("Prefer Gamble", f"Prefer Sure ${amt:,.2f}")
                    key = f"choice_{current}_{st.session_state.phase}_{i}"
                    
                    default_index = None
                    if choices[i] is not None:
                        default_index = 0 if choices[i] == "prospect" else 1
                    
                    st.radio(
                        "Your choice",
                        options=options,
                        index=default_index,
                        horizontal=True,
                        key=key,
                        on_change=on_radio_change,
                        args=(key, i),
                    )

            # Continue button
            if st.button("Continue", use_container_width=True):
                choices = st.session_state.current_choices
                
                # Check all choices made
                if any(c is None for c in choices):
                    st.error("Please answer all questions before continuing.")
                    st.stop()
                
                # Proceed to next phase or problem
                if st.session_state.phase == 1:
                    # Move to phase 2
                    st.session_state.phase1_choices.append(list(choices))
                    st.session_state.phase = 2
                    st.session_state.amounts = generate_sure_amounts(
                        prospect, phase=2, phase1_choices=choices
                    )
                    st.session_state.current_choices = [None] * 7
                    st.rerun()
                else:
                    # Complete current problem
                    ce = compute_certainty_equivalent(choices, amounts)
                    risk_attitude = (
                        "Risk Averse" if ce < ev else
                        "Risk Seeking" if ce > ev else
                        "Risk Neutral"
                    )
                    
                    st.session_state.results.append({
                        "prospect": describe_prospect(prospect),
                        "expected_value": round(ev, 2),
                        "certainty_equivalent": ce,
                        "domain": domain,
                        "risk_attitude": risk_attitude,
                    })
                    
                    # Move to next problem
                    st.session_state.index += 1
                    st.session_state.phase = 1
                    st.session_state.current_choices = [None] * 7
                    
                    if st.session_state.index < total_problems:
                        st.session_state.amounts = generate_sure_amounts(
                            st.session_state.prospects[st.session_state.index], phase=1
                        )
                    st.rerun()