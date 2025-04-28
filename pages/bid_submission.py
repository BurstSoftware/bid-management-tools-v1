# pages/bid_submission.py
import streamlit as st
import pandas as pd
from datetime import datetime

st.header("Subcontractor Bid Submission")

# Manual input form
st.subheader("Manual Bid Entry")
with st.form("bid_form"):
    subcontractor_name = st.text_input("Subcontractor Name")
    cost = st.number_input("Bid Cost (USD)", min_value=0.0, step=1000.0)
    timeline = st.number_input("Timeline (Days)", min_value=1, step=1)
    experience = st.number_input("Experience in Tile Installation (Years)", min_value=0, step=1)
    material_quality = st.slider("Material Quality (1-5, e.g., tile durability)", 1, 5, 3)
    warranty = st.number_input("Warranty on Work (Years)", min_value=0, step=1)
    compliance = st.checkbox("Meets Project Specifications (e.g., tile size, slip resistance)")
    submit_button = st.form_submit_button("Submit Bid")

    if submit_button:
        if subcontractor_name:
            bid = {
                "subcontractor": subcontractor_name,
                "cost": cost,
                "timeline": timeline,
                "experience": experience,
                "material_quality": material_quality,
                "warranty": warranty,
                "compliance": compliance,
                "status": "Submitted",
                "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "score": 0.0
            }
            st.session_state.bids.append(bid)
            st.success(f"Bid from {subcontractor_name} submitted successfully!")
        else:
            st.error("Please provide subcontractor name.")

# CSV upload
st.subheader("Upload Bid (CSV)")
st.write("CSV format: subcontractor,cost,timeline,experience,material_quality,warranty,compliance")
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    required_columns = ["subcontractor", "cost", "timeline", "experience", "material_quality", "warranty", "compliance"]
    if all(col in df.columns for col in required_columns):
        for _, row in df.iterrows():
            bid = {
                "subcontractor": row["subcontractor"],
                "cost": float(row["cost"]),
                "timeline": int(row["timeline"]),
                "experience": int(row["experience"]),
                "material_quality": int(row["material_quality"]),
                "warranty": int(row["warranty"]),
                "compliance": bool(row["compliance"]),
                "status": "Submitted",
                "submitted_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "score": 0.0
            }
            st.session_state.bids.append(bid)
        st.success("Bids uploaded successfully!")
    else:
        st.error(f"CSV must contain columns: {', '.join(required_columns)}")
