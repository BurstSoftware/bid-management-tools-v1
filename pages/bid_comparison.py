# pages/bid_comparison.py
import streamlit as st
import pandas as pd
from utils.scoring import calculate_score

st.header("Bid Comparison")

if st.session_state.bids:
    # Calculate scores
    for bid in st.session_state.bids:
        bid["score"] = calculate_score(bid, st.session_state.bids)
    
    # Create and display DataFrame
    df = pd.DataFrame(st.session_state.bids)
    df = df.sort_values(by="score", ascending=False)
    display_columns = [
        "subcontractor", "cost", "timeline", "experience", "material_quality",
        "warranty", "compliance", "score", "status"
    ]
    st.dataframe(df[display_columns])
    
    # Award contract
    st.subheader("Award Contract")
    selected_subcontractor = st.selectbox("Select Subcontractor to Award", df["subcontractor"])
    if st.button("Award Contract"):
        for bid in st.session_state.bids:
            if bid["subcontractor"] == selected_subcontractor:
                bid["status"] = "Awarded"
            elif bid["status"] != "Submitted":
                bid["status"] = "Reviewed"
        st.success(f"Contract awarded to {selected_subcontractor}!")
else:
    st.warning("No bids submitted yet.")
