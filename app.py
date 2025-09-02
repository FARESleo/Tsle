import streamlit as st
from main_app import render_main_app
from welcome_page import render_welcome_page

st.set_page_config(
    page_title="Smart Money Scanner | SMS",
    page_icon="🧠",
    layout="wide",
)

if 'show_welcome_page' not in st.session_state:
    st.session_state.show_welcome_page = True

# --- CSS مركزي ومحسن ---
if st.session_state.show_welcome_page:
    # --- تصميم احترافي ومستقر لصفحة الترحيب ---
    css = """
        <style>
        header, footer { visibility: hidden; }

        .stApp {
            background: linear-gradient(-45deg, #0f3460, #16213e, #1a1a2e, #274472);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            height: 100vh;
            overflow: hidden; /* منع ظهور أي أشرطة تمرير */
        }

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* حاوية الأيقونات المتحركة */
        .floating-icons {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            pointer-events: none;
        }

        .floating-icons img {
            position: absolute;
            bottom: -100px; /* ابدأ من خارج الشاشة */
            opacity: 0.1;
            animation: float-up 20s infinite linear;
        }

        @keyframes float-up {
            to {
                transform: translateY(-110vh) rotate(360deg);
                opacity: 0;
            }
        }
        
        /* أحجام ومواقع وتأخيرات محددة ومستقرة لكل أيقونة */
        .icon1 { width: 45px; left: 5%; animation-delay: 0s; animation-duration: 25s; }
        .icon2 { width: 70px; left: 15%; animation-delay: 4s; animation-duration: 20s; }
        .icon3 { width: 50px; left: 28%; animation-delay: 8s; animation-duration: 30s; }
        .icon4 { width: 80px; left: 40%; animation-delay: 2s; animation-duration: 18s; }
        .icon5 { width: 60px; left: 55%; animation-delay: 12s; animation-duration: 28s; }
        .icon6 { width: 40px; left: 70%; animation-delay: 6s; animation-duration: 22s; }
        .icon7 { width: 75px; left: 85%; animation-delay: 1s; animation-duration: 19s; }
        .icon8 { width: 55px; left: 95%; animation-delay: 10s; animation-duration: 26s; }


        /* حاوية المحتوى الرئيسي (لحل مشكلة التمرير) */
        .welcome-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 90vh; /* استخدم 90% من ارتفاع الشاشة لتجنب التمرير */
            text-align: center;
            position: relative;
            z-index: 2;
        }

        .glowing-title {
            font-size: 4rem;
            color: #fff;
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 10px #fff, 0 0 20px #007bff, 0 0 30px #007bff; }
            to { text-shadow: 0 0 20px #fff, 0 0 30px #4da8ff, 0 0 40px #4da8ff; }
        }
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
        }}
        </style>
    """

st.markdown(css, unsafe_allow_html=True)

# عرض الصفحة المناسبة
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
