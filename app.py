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

# --- تحميل إعدادات المستخدمين ---
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("خطأ: لم يتم العثور على ملف الإعدادات 'config.yaml'.")
    st.stop()

# --- تهيئة أداة المصادقة ---
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# --- المنطق الجديد للتحكم في العرض ---

# التحقق مما إذا كان المستخدم قد سجل دخوله بالفعل
if st.session_state.get("authentication_status"):
    # إذا كان مسجلاً، اعرض التطبيق الرئيسي
    render_main_app()
    with st.sidebar:
        st.write(f'أهلاً بك *{st.session_state["name"]}*')
        authenticator.logout('تسجيل الخروج', 'main')
else:
    # إذا لم يكن مسجلاً، قم بعرض الصفحة الترحيبية أولاً
    render_welcome_page()

    # اعرض نموذج تسجيل الدخول في مكان مخصص وواضح
    st.markdown("---")
    _, center_col, _ = st.columns([1, 1.5, 1])
    with center_col:
        st.markdown("<h2 style='text-align: center;'>تسجيل الدخول للمتابعة</h2>", unsafe_allow_html=True)
        name, authentication_status, username = authenticator.login('main')
        
        if st.session_state["authentication_status"] is False:
            st.error('اسم المستخدم أو كلمة المرور غير صحيحة')
        elif st.session_state["authentication_status"] is None:
            st.info('الرجاء إدخال اسم المستخدم وكلمة المرور')
