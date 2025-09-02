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

# --- CSS بسيط جداً ومستقر ---
# هذا الكود مسؤول فقط عن الخلفية وإخفاء العناصر غير المرغوب فيها
if st.session_state.show_welcome_page:
    css = """
        <style>
        /* إخفاء الشريط العلوي والسفلي */
        header, footer { visibility: hidden; }
        
        /* خلفية داكنة وأنيقة */
        .stApp {
            background-color: #0a0a0f;
        }
        
        /* إزالة المسافات البيضاء الزائدة في أعلى وأسفل الصفحة */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* لتوسيط الصور داخل الأعمدة */
        div[data-testid="stHorizontalBlock"] {
            align-items: center;
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
