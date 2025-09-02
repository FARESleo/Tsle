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

# --- CSS مركزي ---
# اختر رابط الخلفية بناءً على الصفحة الحالية
if st.session_state.show_welcome_page:
    background_url = "https://i.imgur.com/Ra9blqc.png" # خلفية صفحة الترحيب
    css = """
        <style>
        .stApp {
            background-image: url("%s");
            background-size: cover;
        }
        /* إخفاء الشريط العلوي والسفلي */
        header, footer { visibility: hidden; }
        </style>
    """ % background_url
else:
    background_url = "https://i.imgur.com/Utvjk6E.png" # خلفية التطبيق الرئيسي
    css = """
        <style>
        .stApp {
            background-image: url("%s");
            background-size: cover;
            background-attachment: fixed;
        }
        /* إخفاء الشريط العلوي والسفلي أيضاً هنا */
        header, footer { visibility: hidden; }
        </style>
    """ % background_url

# تطبيق الـ CSS
st.markdown(css, unsafe_allow_html=True)


# Display the appropriate page based on the session state
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
