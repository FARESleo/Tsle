import streamlit as st
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


# --- تحميل ملف CSS المركزي ---
load_css("style.css")

if 'show_welcome_page' not in st.session_state:
    st.session_state.show_welcome_page = True

# عرض الصفحة المناسبة وتطبيق الـ class الخاص بالخلفية
if st.session_state.show_welcome_page:
    st.markdown('<div class="welcome-page-container">', unsafe_allow_html=True)
    render_welcome_page()
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="main-app-container">', unsafe_allow_html=True)
    render_main_app()
    st.markdown('</div>', unsafe_allow_html=True)
