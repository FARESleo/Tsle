import streamlit as st
from main_app import render_main_app
from welcome_page import render_welcome_page

# Set the basic configuration for the page
st.set_page_config(
    page_title="Smart Money Scanner | SMS",
    page_icon="🧠",
    layout="wide",
)

# Initialize the session state to switch between pages
if 'show_welcome_page' not in st.session_state:
    st.session_state.show_welcome_page = True

# --- CSS مركزي ومحسّن ---

if st.session_state.show_welcome_page:
    # --- تصميم احترافي ومتقدم لصفحة الترحيب ---
    background_url = "https://i.imgur.com/Ra9blqc.png"
    css = f"""
        <style>
        /* إخفاء الشريط العلوي والسفلي */
        header, footer {{ visibility: hidden; }}

        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* حاوية أيقونات العملات المتحركة */
        .floating-icons {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: 1;
        }}

        .floating-icons img {{
            position: absolute;
            bottom: -150px; /* ابدأ من خارج الشاشة */
            opacity: 0.15; /* شفافية خفيفة */
            animation: float-up 25s infinite linear;
        }}

        /* تحديد أحجام وأماكن عشوائية للأيقونات */
        .floating-icons img:nth-child(1) {{ left: 5%; width: 80px; animation-delay: 0s; }}
        .floating-icons img:nth-child(2) {{ left: 15%; width: 40px; animation-delay: 5s; animation-duration: 30s; }}
        .floating-icons img:nth-child(3) {{ left: 25%; width: 60px; animation-delay: 10s; }}
        .floating-icons img:nth-child(4) {{ left: 40%; width: 90px; animation-delay: 2s; animation-duration: 20s; }}
        .floating-icons img:nth-child(5) {{ left: 60%; width: 50px; animation-delay: 15s; }}
        .floating-icons img:nth-child(6) {{ left: 75%; width: 70px; animation-delay: 8s; animation-duration: 35s; }}
        .floating-icons img:nth-child(7) {{ left: 90%; width: 45px; animation-delay: 12s; }}

        /* تعريف حركة الصعود للأعلى */
        @keyframes float-up {{
            to {{
                transform: translateY(-120vh); /* تحرك لمسافة تتجاوز ارتفاع الشاشة */
            }}
        }}

        /* تصميم العنوان الرئيسي المتوهج */
        .glowing-title {{
            font-size: 4rem;
            color: #fff;
            text-align: center;
            animation: glow 2s ease-in-out infinite alternate;
        }}
        
        /* تعريف حركة التوهج */
        @keyframes glow {{
            from {{
                text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #007bff, 0 0 40px #007bff, 0 0 50px #007bff, 0 0 60px #007bff, 0 0 70px #007bff;
            }}
            to {{
                text-shadow: 0 0 20px #fff, 0 0 30px #4da8ff, 0 0 40px #4da8ff, 0 0 50px #4da8ff, 0 0 60px #4da8ff, 0 0 70px #4da8ff, 0 0 80px #4da8ff;
            }}
        }}
        
        .welcome-container {{
            position: relative;
            z-index: 2; /* تأكد من أن المحتوى فوق الأيقونات المتحركة */
        }}

        </style>
    """
else:
    # --- CSS العادي للصفحة الرئيسية ---
    background_url = "https://i.imgur.com/Utvjk6E.png"
    css = f"""
        <style>
        header, footer {{ visibility: hidden; }}
        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
    """

# تطبيق الـ CSS
st.markdown(css, unsafe_allow_html=True)


# عرض الصفحة المناسبة
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
