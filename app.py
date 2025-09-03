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

# --- عرض نموذج تسجيل الدخول ---
# سيتم عرض هذا النموذج في الشريط الجانبي لكي لا يؤثر على تصميمك
name, authentication_status, username = authenticator.login('Login', 'sidebar')

# --- التحقق من حالة تسجيل الدخول ---
if st.session_state["authentication_status"]:
    # --- الحالة: تسجيل الدخول ناجح ---
    
    # إخفاء الشريط الجانبي بعد الدخول الناجح وإظهار زر الخروج فقط
    st.markdown("<style>div[data-testid='stSidebarNav'] {display: none;}</style>", unsafe_allow_html=True)
    with st.sidebar:
        st.write(f'Welcome *{st.session_state["name"]}*')
        authenticator.logout('Logout', 'main')
    
    # اعرض التطبيق الرئيسي الكامل للتحليلات
    render_main_app()
    
elif st.session_state["authentication_status"] is False:
    # --- الحالة: خطأ في تسجيل الدخول ---
    with st.sidebar:
        st.error('Username/password is incorrect')
    render_welcome_page()

elif st.session_state["authentication_status"] is None:
    # --- الحالة: لم يتم تسجيل الدخول بعد ---
    render_welcome_page()
