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
    st.error("Error: The 'config.yaml' file was not found.")
    st.stop()

# --- تهيئة أداة المصادقة ---
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# --- المنطق النهائي للتحكم في العرض ---
if st.session_state.get("authentication_status"):
    # --- الكود الجديد: تخزين حالة الاشتراك ---
    try:
        user_details = config['credentials']['usernames'][st.session_state['username']]
        st.session_state['subscription'] = user_details.get('subscription', 'Free')
    except KeyError:
        # حالة احتياطية إذا لم يتم العثور على المستخدم
        st.session_state['subscription'] = 'Free'
    # --- نهاية الكود الجديد ---

    render_main_app()
    with st.sidebar:
        st.write(f'أهلاً بك *{st.session_state["name"]}*')
        authenticator.logout('تسجيل الخروج', 'main')
else:
    render_welcome_page(authenticator)
