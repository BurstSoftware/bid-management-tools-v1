# pages/project_baseline_setup.py
import streamlit as st
import pandas as pd

st.header("Project Baseline (Cost Estimator Integration)")

baseline_cost = st.number_input(
    "Enter Project Baseline Cost (USD)",
    min_value=0.0,
    value=st.session_state.project_baseline,
    step=1000.0
)
if st.button("Save Baseline"):
    st.session_state.project_baseline = baseline_cost
    st.success(f"Project baseline set to ${baseline_cost:,.2f}")

# Compare bids to baseline
st.write(f"Current Baseline Cost: ${st.session_state.project_baseline:,.2f}")
if st.session_state.bids:
    df = pd.DataFrame(st.session_state.bids)
    df["cost_vs_baseline"] = df["cost"] - st.session_state.project_baseline
    st.dataframe(df[["subcontractor", "cost", "cost_vs_baseline"]])
