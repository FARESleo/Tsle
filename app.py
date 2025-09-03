import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

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
        st.session_state['subscription'] = 'Free'
    # --- نهاية الكود الجديد ---

    # --- القائمة الجديدة للمستخدم ---
    _, col2 = st.columns([6, 1])
    with col2:
        selected_option = option_menu(
            menu_title=None,
            options=["ملفي الشخصي", "تسجيل الخروج"],
            icons=['person-circle', 'box-arrow-right'],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "transparent"},
                "icon": {"color": "white", "font-size": "18px"}, 
                "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#333"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )
    
    # --- التعامل مع اختيار المستخدم (النسخة المُعدّلة) ---
    if selected_option == "تسجيل الخروج":
        # نقوم بتسجيل الخروج مباشرة عبر إعادة تعيين حالة المصادقة
        st.session_state['authentication_status'] = None
        st.session_state['name'] = None
        st.session_state['username'] = None
        st.rerun() # إعادة تشغيل التطبيق للعودة إلى الصفحة الترحيبية
        
    elif selected_option == "ملفي الشخصي":
        st.toast("سيتم إضافة صفحة الملف الشخصي قريبًا!", icon="⏳")

    # عرض التطبيق الرئيسي
    render_main_app()

else:
    # إذا لم يسجل دخوله، اعرض الصفحة الترحيبية
    render_welcome_page(authenticator)
