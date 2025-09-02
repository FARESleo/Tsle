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

# --- CSS مركزي ومحسن ---
if st.session_state.show_welcome_page:
    # --- تصميم أنيق ومستقر لصفحة الترحيب ---
    css = """
        <style>
        header, footer { visibility: hidden; }

        .stApp {
            background: radial-gradient(circle at center, #1a1a2e, #0a0a0f);
            height: 100vh;
            overflow: hidden; /* منع التمرير نهائياً */
        }

        .welcome-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }

        .glowing-title {
            font-size: 4.5rem;
            color: #fff;
            margin-bottom: 1rem;
            text-shadow: 0 0 10px #fff, 0 0 20px #007bff, 0 0 30px #007bff;
        }

        .welcome-subtitle {
            font-size: 1.5rem;
            color: #cccccc;
            margin-bottom: 3rem;
            text-shadow: 1px 1px 2px #000;
        }

        .crypto-icons-row {
            display: flex;
            justify-content: center;
            gap: 25px; /* مسافة بين الأيقونات */
            margin-bottom: 4rem;
        }

        .crypto-icons-row img {
            width: 55px;
            height: 55px;
            filter: drop-shadow(0 0 10px rgba(0, 123, 255, 0.6));
            transition: transform 0.3s ease;
        }

        .crypto-icons-row img:hover {
            transform: scale(1.2) rotate(10deg);
        }

        .stButton>button {
            border: 2px solid #007bff;
            border-radius: 50px;
            padding: 15px 40px;
            font-size: 1.3rem;
            font-weight: bold;
            color: white;
            background: transparent;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 0 15px #007bff;
        }
        .stButton>button:hover {
            background: #007bff;
            box-shadow: 0 0 25px #007bff;
            transform: scale(1.05);
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
