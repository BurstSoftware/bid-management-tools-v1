# app.py
import streamlit as st

# Initialize shared state
if "bids" not in st.session_state:
    st.session_state.bids = []
if "project_baseline" not in st.session_state:
    st.session_state.project_baseline = 100000.0  # Changed to float

# App title
st.title("Bid Management Tool for Tile Installation")

# Sidebar navigation (Streamlit auto-detects pages in the 'pages/' folder)
st.sidebar.header("Bidding Process")
st.sidebar.write("Select a page from the menu above.")

# Footer
st.sidebar.write("Bid Management Tool v2.0 | Tile Installation")
