import streamlit as st
# تم تصحيح اسم الملف هنا من main-app إلى main_app
from main_app import render_main_app 
from welcome_page import render_welcome_page

st.set_page_config(
    page_title="Signal Prime | Smart Money Scanner",
    page_icon="🧠",
    layout="wide",
)

# دالة لتحميل CSS من ملف خارجي
def load_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"خطأ: لم يتم العثور على ملف التصميم '{file_name}'. تأكد من وجوده في نفس المجلد.")

# --- تحميل ملف CSS المركزي للمكونات ---
load_css("style.css")

if 'show_welcome_page' not in st.session_state:
    st.session_state.show_welcome_page = True

# --- تطبيق خلفية الصفحة المناسبة ديناميكيًا ---
if st.session_state.show_welcome_page:
    # تطبيق الخلفية الداكنة للصفحة الترحيبية
    st.markdown("""
        <style>
        .stApp {
            background-color: #0a0a0f;
            overflow: hidden;
        }
        </style>
    """, unsafe_allow_html=True)
    render_welcome_page()
else:
    # تطبيق صورة الخلفية للتطبيق الرئيسي
    background_url = "https://i.imgur.com/Utvjk6E.png"
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)
    render_main_app()
