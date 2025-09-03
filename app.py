import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# -- استيراد الدوال من ملفاتك --
from main_app import render_main_app
from welcome_page import render_welcome_page

st.set_page_config(
    page_title="Signal Prime | Smart Money Scanner",
    page_icon="🧠",
    layout="wide",
)

# --- تحميل إعدادات المستخدمين من ملف config.yaml ---
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("خطأ: لم يتم العثور على ملف الإعدادات 'config.yaml'.")
    st.stop()

# --- تهيئة أداة المصادقة (بدون preauthorized) ---
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# --- عرض نموذج تسجيل الدخول ---
authenticator.login('main')

# --- التحقق من حالة تسجيل الدخول (الطريقة الصحيحة) ---

if st.session_state["authentication_status"]:
    # --- الحالة: تسجيل الدخول ناجح ---
    
    # 1. اعرض التطبيق الرئيسي الكامل
    render_main_app()
    
    # 2. أضف زر تسجيل الخروج في الشريط الجانبي
    with st.sidebar:
        st.write(f'أهلاً بك *{st.session_state["name"]}*')
        st.title("") # مسافة
        authenticator.logout('تسجيل الخروج', 'main')

elif st.session_state["authentication_status"] is False:
    # --- الحالة: خطأ في تسجيل الدخول ---
    st.error('اسم المستخدم أو كلمة المرور غير صحيحة')
    try:
        render_welcome_page()
    except Exception as e:
        st.error(e)

elif st.session_state["authentication_status"] is None:
    # --- الحالة: لم يتم تسجيل الدخول بعد ---
    try:
        render_welcome_page()
    except Exception as e:
        st.error(e)
