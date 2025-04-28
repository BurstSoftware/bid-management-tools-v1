# pages/bid_analysis_report.py
import streamlit as st
import pandas as pd
from utils.scoring import calculate_score

st.header("Bid Analysis Report")

if st.session_state.bids:
    # Calculate scores
    for bid in st.session_state.bids:
        bid["score"] = calculate_score(bid, st.session_state.bids)
    
    # Generate report
    df = pd.DataFrame(st.session_state.bids)
    df = df.sort_values(by="score", ascending=False)
    df["cost_vs_baseline"] = df["cost"] - st.session_state.project_baseline
    display_columns = [
        "subcontractor", "cost", "timeline", "experience", "material_quality",
        "warranty", "compliance", "score", "status", "submitted_at", "cost_vs_baseline"
    ]
    st.dataframe(df[display_columns])
    
    # Download report
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Bid Analysis Report",
        data=csv,
        file_name="bid_analysis_report.csv",
        mime="text/csv"
    )
else:
    st.warning("No bids available for analysis.")
