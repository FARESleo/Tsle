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
            menu_icon="cast", # يمكن تغيير هذا الرمز العام للقائمة إذا أردت
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "transparent", "justify-content": "flex-end"},
                "icon": {"color": "#bbbbbb", "font-size": "18px"}, # لون أيقونات عام
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "center",
                    "margin": "0px 5px", # مسافة بين الأزرار
                    "--hover-color": "#2a2a2a", # لون الخلفية عند الوقوف بالماوس
                    "color": "#e0e0e0", # لون النص العام
                    "background-color": "#1a1a1a", # خلفية الأزرار العادية
                    "border-radius": "8px", # حواف مستديرة
                    "padding": "8px 15px", # مسافة داخلية
                    "transition": "background-color 0.3s, color 0.3s" # انتقال سلس
                },
                "nav-link-selected": {
                    "background-color": "#007bff", # اللون الأزرق الذي تستخدمه في أماكن أخرى
                    "color": "white", # نص أبيض
                    "font-weight": "bold",
                    "border-radius": "8px",
                },
                # يمكن إضافة المزيد من التعديلات هنا
            }
        )
    
    # التعامل مع اختيار المستخدم
    if selected_option == "تسجيل الخروج":
        authenticator.logout('تسجيل الخروج', 'main')
        st.rerun()
    elif selected_option == "ملفي الشخصي":
        st.toast("سيتم إضافة صفحة الملف الشخصي قريبًا!", icon="⏳")

    # عرض التطبيق الرئيسي
    render_main_app()

else:
    # إذا لم يسجل دخوله، اعرض الصفحة الترحيبية
    render_welcome_page(authenticator)
