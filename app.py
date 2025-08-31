import streamlit as st
from main_app import render_main_app
from welcome_page import render_welcome_page

# Set the basic configuration for the page
st.set_page_config(
    page_title="Smart Money Scanner | SMS",
    page_icon="🧠",
    layout="wide",
)

# Initialize the session state to switch between pages
if 'show_welcome_page' not in st.session_state:
    st.session_state.show_welcome_page = True

# Display the appropriate page based on the session state
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
