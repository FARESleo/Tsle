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

# --- التحقق المبدئي من حالة تسجيل الدخول ---
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

# --- المنطق الصحيح والنهائي ---
if st.session_state["authentication_status"]:
    # --- الحالة: تسجيل الدخول ناجح ---
    with st.sidebar:
        st.write(f'أهلاً بك *{st.session_state["name"]}*')
        # الاستدعاء الصحيح لدالة الخروج
        authenticator.logout(button_name='تسجيل الخروج', location='main')
    
    render_main_app()
    
else:
    # --- الحالة: لم يتم تسجيل الدخول بعد أو فشل الدخول ---
    try:
        # الاستدعاء الصحيح لدالة الدخول
        name, authentication_status, username = authenticator.login(form_name='Login', location='sidebar')
        
        if st.session_state["authentication_status"] is False:
            with st.sidebar:
                st.error('اسم المستخدم أو كلمة المرور غير صحيحة')
        
        # اعرض الصفحة الترحيبية دائمًا إذا لم يكن المستخدم قد سجل دخوله
        render_welcome_page()

    except Exception as e:
        st.error(e)
