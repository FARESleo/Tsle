import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

from main_app import render_main_app
from welcome_page import render_welcome_page

st.set_page_config(
    page_title="Signal Prime | Smart Money Scanner",
    page_icon="🧠",
    layout="wide",
)

# --- Load user credentials ---
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("Error: The 'config.yaml' file was not found. Please create it.")
    st.stop()

# --- Initialize the authenticator ---
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# --- Render the login module ---
# The location is now correctly passed as a keyword argument 'location'
name, authentication_status, username = authenticator.login(location='sidebar')

# --- Check the authentication status ---
if st.session_state["authentication_status"]:
    # --- State: Successful login ---
    
    # Hide the sidebar navigation and show the logout button
    st.markdown("<style>div[data-testid='stSidebarNav'] {display: none;}</style>", unsafe_allow_html=True)
    with st.sidebar:
        st.write(f'Welcome *{st.session_state["name"]}*')
        authenticator.logout('Logout', 'main')
    
    # Render the main analysis app
    render_main_app()
    
elif st.session_state["authentication_status"] is False:
    # --- State: Incorrect password/username ---
    with st.sidebar:
        st.error('Username/password is incorrect')
    render_welcome_page()

elif st.session_state["authentication_status"] is None:
    # --- State: No login attempt yet ---
    render_welcome_page()
