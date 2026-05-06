import streamlit as st
import pandas as pd

# Global Ranking Range
LOWEST_RANK = 1
HIGHEST_RANK = 5

st.set_page_config(page_title="MCDA Decision Maker", layout="wide")

st.title("MCDA Decision Maker")
st.write("Determine the best choice based on your custom categories.")

# --- INITIALIZING SESSION STATE ---
if 'options' not in st.session_state:
    st.session_state.options = []
if 'categories' not in st.session_state:
    st.session_state.categories = []
if 'df' not in st.session_state:
    st.session_state.df = None

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.header("1. Setup")
    
    # Input for Options
    new_option = st.text_input("Enter an Option (e.g., Car A):")
    if st.button("Add Option"):
        if new_option and new_option not in st.session_state.options:
            st.session_state.options.append(new_option)
    
    # Input for Categories
    new_cat = st.text_input("Enter a Category (e.g., Safety):")
    if st.button("Add Category"):
        if new_cat and new_cat not in st.session_state.categories:
            st.session_state.categories.append(new_cat)

    if st.button("Clear All"):
        st.session_state.options = []
        st.session_state.categories = []
        st.session_state.df = None
        st.rerun()

# --- DATA ENTRY TABLE ---
if st.session_state.options and st.session_state.categories:
    st.header("2. Enter Ratings")
    st.info(f"Enter scores from {LOWEST_RANK} to {HIGHEST_RANK}")

    # Initialize the DataFrame if it doesn't exist
    if st.session_state.df is None or st.session_state.df.shape != (len(st.session_state.categories), len(st.session_state.options)):
        st.session_state.df = pd.DataFrame(
            0.0, 
            index=st.session_state.categories, 
            columns=st.session_state.options
        )

    # Use st.data_editor to allow users to type directly into the table!
    edited_df = st.data_editor(st.session_state.df, use_container_width=True)
    st.session_state.df = edited_df

    # --- ANALYSIS ---
    if st.button("Calculate Winner"):
        st.divider()
        
        # Calculate Averages
        averages = edited_df.mean(axis=0)
        
        # Determine Winner
        winner_name = averages.idxmax()
        winner_score = averages.max()

        # Display Results
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Summary Table")
            
            # HIGHLIGHTING LOGIC
            def highlight_max(s):
                is_max = s == s.max()
                return ['background-color: #2e7d32; color: white' if v else '' for v in is_max]

            # Convert averages to a DF for styled display
            avg_df = pd.DataFrame(averages, columns=["Average Score"]).T
            st.dataframe(avg_df.style.apply(highlight_max, axis=1))

        with col2:
            st.success(f"### 🏆 The Winner is: **{winner_name.upper()}**")
            st.metric(label="Highest Average Score", value=f"{winner_score:.2f}")

else:
    st.warning("Please add at least one Option and one Category in the sidebar to begin.")