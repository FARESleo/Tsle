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
        /* إخفاء العناصر الافتراضية */
        header, footer { visibility: hidden; }

        /* خلفية داكنة وأنيقة */
        .stApp {
            background-color: #0a0a0f;
            overflow: hidden; /* منع التمرير نهائياً */
        }
        
        /* إزالة المسافات الزائدة في أعلى الصفحة */
        .block-container {
            padding-top: 2rem;
        }

        /* تصميم الزر */
        .stButton>button {
            border: 2px solid #007bff;
            border-radius: 50px;
            padding: 10px 30px;
            font-size: 1.1rem;
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
    st.markdown(css, unsafe_allow_html=True)
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
