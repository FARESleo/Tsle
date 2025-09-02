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
# خصائص مشتركة للخلفية في كل الصفحات
common_css = """
    /* إخفاء الشريط العلوي والسفلي */
    header, footer { visibility: hidden; }

    .stApp {
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
"""

# اختر رابط الخلفية وحجمها بناءً على الصفحة الحالية
if st.session_state.show_welcome_page:
    background_url = "https://i.imgur.com/Ra9blqc.png"
    # (هذا هو التعديل) استخدام contain لعرض الصورة كاملة دون قص (زوم)
    background_size = "contain"
else:
    background_url = "https://i.imgur.com/Utvjk6E.png"
    # استخدام cover لملء الشاشة بالكامل في الصفحة الرئيسية
    background_size = "cover"


# تطبيق الـ CSS مع الخلفية المحددة
st.markdown(f"""
    <style>
    {common_css}
    .stApp {{
        background-image: url("{background_url}");
        background-size: {background_size};
    }}
    </style>
    """, unsafe_allow_html=True)


# Display the appropriate page based on the session state
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
