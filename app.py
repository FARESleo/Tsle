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
    # --- تصميم احترافي بخلفية حيوية وأنيميشن للأيقونات ---
    css = """
        <style>
        /* إخفاء العناصر الافتراضية */
        header, footer { visibility: hidden; }

        /* الخلفية الحيوية */
        .stApp {
            background-color: #000011; /* لون أساسي داكن */
            overflow: hidden;
            position: relative;
        }

        .background-animation {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
        }

        .circle {
            position: absolute;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(0,123,255,0.4) 0%, rgba(0,123,255,0) 70%);
            animation: move 20s infinite linear;
        }
        
        .circle.c1 { width: 400px; height: 400px; top: 20%; left: 10%; animation-duration: 25s; }
        .circle.c2 { width: 300px; height: 300px; top: 50%; left: 50%; animation-duration: 30s; }
        .circle.c3 { width: 500px; height: 500px; top: 80%; left: 80%; animation-duration: 20s; }
        .circle.c4 { width: 250px; height: 250px; top: 10%; left: 70%; animation-duration: 35s; }

        @keyframes move {
            0% { transform: translate(0, 0); }
            25% { transform: translate(20px, 40px); }
            50% { transform: translate(-30px, -10px); }
            75% { transform: translate(10px, -50px); }
            100% { transform: translate(0, 0); }
        }

        /* حاوية الأيقونات المتحركة */
        .floating-icons {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: 1;
        }

        .floating-icons img {
            position: absolute;
            bottom: -150px;
            opacity: 0.15;
            animation: float-up 25s infinite linear;
            animation-delay: var(--delay);
            width: var(--size);
        }

        @keyframes float-up {
            to {
                transform: translateY(-120vh) rotate(360deg);
                opacity: 0;
            }
        }

        /* تصميم العنوان والمحتوى */
        .welcome-container, .glowing-title, .welcome-subtitle, .stButton {
            position: relative;
            z-index: 2;
        }

        .glowing-title {
            font-size: 4rem;
            color: #fff;
            text-align: center;
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
