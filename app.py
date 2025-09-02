import streamlit as st
from main_app import render_main_app
from welcome_page import render_welcome_page

st.set_page_config(
    page_title="Signal Prime | Smart Money Scanner",
    page_icon="🧠",
    layout="wide",
)

if 'show_welcome_page' not in st.session_state:
    st.session_state.show_welcome_page = True

# --- CSS مركزي ومفصول تماماً لكل صفحة ---
if st.session_state.show_welcome_page:
    # --- تصميم أنيق ومستقر لصفحة الترحيب مع خلفية فيديو ---
    css = """
        <style>
        /* إخفاء العناصر الافتراضية */
        header, footer { visibility: hidden; }

        /* حاوية الفيديو لتغطية كامل الشاشة */
        #video-background {
            position: fixed;
            top: 50%;
            left: 50%;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -1;
            transform: translateX(-50%) translateY(-50%);
            background-size: cover;
        }

        /* فلتر داكن فوق الفيديو لإبراز النص */
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 10, 0.6); /* لون أسود مزرق شبه شفاف */
            z-index: 0;
        }

        /* حاوية المحتوى لتوسيط كل شيء */
        .welcome-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
            position: relative;
            z-index: 1;
        }

        /* تصميم العنوان والنص التحفيزي */
        .glowing-title {
            font-size: 4.5rem;
            color: #fff;
            text-shadow: 0 0 10px #fff, 0 0 25px #4da8ff;
        }
        .welcome-subtitle {
            font-size: 1.5rem;
            color: #cccccc;
            margin-top: -10px;
        }
        
        /* تصميم الزر */
        .stButton>button {
            border: 2px solid #007bff;
            border-radius: 50px;
            padding: 15px 40px;
            font-size: 1.3rem;
            color: white;
            background: transparent;
            transition: all 0.3s ease;
            margin-top: 40px;
        }
        .stButton>button:hover {
            background: #007bff;
            box-shadow: 0 0 20px #007bff;
        }
        </style>
    """
else:
    # --- CSS العادي والمستقر للصفحة الرئيسية (تم إصلاح الخلفية) ---
    background_url = "https://i.imgur.com/Utvjk6E.png"
    css = f"""
        <style>
        header, footer { visibility: hidden; }
        .stApp {
            background-image: url("{background_url}");
            background-size: cover; /* تم إصلاح المشكلة هنا */
            background-position: center;
            background-attachment: fixed;
        }
        </style>
    """

st.markdown(css, unsafe_allow_html=True)

# عرض الصفحة المناسبة
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
