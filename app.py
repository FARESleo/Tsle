import streamlit as st
from main_app import render_main_app
from welcome_page import render_welcome_page

st.set_page_config(
    page_title="Smart Money Scanner | SMS",
    page_icon="🧠",
    layout="wide",
)

if 'show_welcome_page' not in st.session_state:
    st.session_state.show_welcome_page = True

# --- CSS مركزي ومحسن ---
if st.session_state.show_welcome_page:
    # --- تصميم احترافي بخلفية متدرجة متحركة ---
    css = """
        <style>
        header, footer { visibility: hidden; }

        .stApp {
            background: linear-gradient(-45deg, #0f3460, #16213e, #1a1a2e, #274472);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            height: 100vh;
        }

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .glowing-title {
            font-size: 4rem;
            color: #fff;
            text-align: center;
            animation: glow 2s ease-in-out infinite alternate;
            position: relative;
            z-index: 2;
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 10px #fff, 0 0 20px #007bff, 0 0 30px #007bff; }
            to { text-shadow: 0 0 20px #fff, 0 0 30px #4da8ff, 0 0 40px #4da8ff; }
        }
        </style>
    """
else:
    # --- CSS العادي للصفحة الرئيسية ---
    background_url = "https://i.imgur.com/Utvjk6E.png"
    css = f"""
        <style>
        header, footer {{ visibility: hidden; }}
        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
        }}
        </style>
    """

st.markdown(css, unsafe_allow_html=True)

# عرض الصفحة المناسبة
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
