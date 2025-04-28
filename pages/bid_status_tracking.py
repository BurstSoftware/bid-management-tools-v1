# pages/bid_status_tracking.py
import streamlit as st
import pandas as pd

st.header("Bid Status Tracking")

if st.session_state.bids:
    df = pd.DataFrame(st.session_state.bids)
    display_columns = [
        "subcontractor", "status", "submitted_at", "cost", "timeline",
        "experience", "material_quality", "warranty"
    ]
    st.dataframe(df[display_columns])
else:
    st.warning("No bids to track.")
