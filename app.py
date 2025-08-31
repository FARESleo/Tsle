# frontend/app.py
import streamlit as st
from main_app import render_main_app
from welcome_page import render_welcome_page

# الإعدادات الأساسية لعنوان الصفحة
st.set_page_config(
    page_title="Smart Money Scanner | SMS",
    page_icon="🧠",
    layout="wide",
)

# تهيئة حالة الجلسة للتبديل بين الصفحات
if 'show_welcome_page' not in st.session_state:
    st.session_state.show_welcome_page = True

# عرض الصفحة المناسبة بناءً على حالة الجلسة
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
