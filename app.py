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

# --- CSS مركزي ومحسّن ---
# هذا هو الكود الجديد الذي يضمن عرض الخلفية بشكل أفضل
common_css = """
    /* إخفاء الشريط العلوي والسفلي */
    header, footer { visibility: hidden; }

    .stApp {
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
"""

# اختر رابط الخلفية بناءً على الصفحة الحالية
if st.session_state.show_welcome_page:
    background_url = "https://i.imgur.com/Ra9blqc.png"
else:
    background_url = "https://i.imgur.com/Utvjk6E.png"

# تطبيق الـ CSS مع الخلفية المحددة
st.markdown(f"""
    <style>
    {common_css}
    .stApp {{
        background-image: url("{background_url}");
    }}
    </style>
    """, unsafe_allow_html=True)


# Display the appropriate page based on the session state
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
