import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

from main_app import render_main_app
from welcome_page import render_welcome_page

st.set_page_config(
    page_title="Signal Prime | Smart Money Scanner",
    page_icon="🧠",
    layout="wide",
)

# --- تحميل إعدادات المستخدمين ---
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("Error: The 'config.yaml' file was not found. Please create it.")
    st.stop()

# --- تهيئة أداة المصادقة ---
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# --- عرض نموذج تسجيل الدخول في الشريط الجانبي ---
# هذه الدالة تقوم بعرض النموذج وتحديث حالة الدخول داخليًا
authenticator.login(location='sidebar')

# --- التحقق من حالة الدخول من st.session_state ---

if st.session_state["authentication_status"]:
    # --- الحالة: تسجيل الدخول ناجح ---
    
    # عرض زر الخروج في الشريط الجانبي
    with st.sidebar:
        st.write(f'أهلاً بك *{st.session_state["name"]}*')
        authenticator.logout(button_name='تسجيل الخروج', location='main')
    
    # عرض التطبيق الرئيسي للتحليلات
    render_main_app()
    
elif st.session_state["authentication_status"] is False:
    # --- الحالة: خطأ في تسجيل الدخول ---
    with st.sidebar:
        st.error('اسم المستخدم أو كلمة المرور غير صحيحة')
    # عرض الصفحة الترحيبية
    render_welcome_page()

elif st.session_state["authentication_status"] is None:
    # --- الحالة: لم يتم تسجيل الدخول بعد ---
    with st.sidebar:
        st.info('الرجاء تسجيل الدخول للوصول إلى الماسح الضوئي.')
    # عرض الصفحة الترحيبية
    render_welcome_page()
