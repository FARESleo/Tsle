import streamlit as st
from main_app import render_main_app
from welcome_page import render_welcome_page

st.set_page_config(
    page_title="Signal Prime | Smart Money Scanner",
    page_icon="🧠",
    layout="wide",
)

if 'show_welcome_page' not in st.session_state:
    st.session_state.show_welcome_page = True

# --- CSS بسيط ومستقر ---
if st.session_state.show_welcome_page:
    # CSS لصفحة الترحيب يتم حقنه من welcome_page.py مباشرة
    pass  # لا حاجة لأي CSS هنا بعد الآن
else:
    # --- CSS العادي للصفحة الرئيسية ---
    background_url = "https://i.imgur.com/Utvjk6E.png"
    css = f"""
        <style>
        header, footer {{ visibility: hidden; }}
        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# عرض الصفحة المناسبة
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
