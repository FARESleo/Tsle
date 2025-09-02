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

# --- CSS مركزي ومحسن ---
if st.session_state.show_welcome_page:
    # --- تصميم احترافي ومستقر لصفحة الترحيب ---
    css = """
        <style>
        header, footer { visibility: hidden; }

        /* --- الخلفية الحيوية بتأثير المجرة الرقمية --- */
        @keyframes move-twink-back {
            from {background-position:0 0;}
            to {background-position:-10000px 5000px;}
        }

        .stars, .twinkling {
            position:absolute;
            top:0;
            left:0;
            right:0;
            bottom:0;
            width:100%;
            height:100%;
            display:block;
            z-index: 0;
        }

        .stars {
            background:#000 url(https://i.imgur.com/h6FudH5.png) repeat top center;
        }

        .twinkling{
            background:transparent url(https://i.imgur.com/f0IhyT2.png) repeat top center;
            animation:move-twink-back 200s linear infinite;
        }

        /* حاوية المحتوى الرئيسي (لحل مشكلة التمرير) */
        .welcome-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 95vh; /* استخدم 95% من ارتفاع الشاشة لتجنب التمرير */
            text-align: center;
            position: relative;
            z-index: 2;
        }

        /* --- تصميم النصوص المتوهجة --- */
        .glowing-title {
            font-size: 4.5rem;
            color: #fff;
            animation: glow 1.5s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 10px #fff, 0 0 20px #007bff, 0 0 30px #007bff; }
            to { text-shadow: 0 0 20px #fff, 0 0 35px #4da8ff, 0 0 45px #4da8ff; }
        }

        /* --- تصميم زر البدء الاحترافي --- */
        .stButton>button {
            border: 2px solid #007bff;
            border-radius: 50px;
            padding: 15px 35px;
            font-size: 1.2rem;
            font-weight: bold;
            color: white;
            background: transparent;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 0 10px #007bff, inset 0 0 10px #007bff;
        }
        .stButton>button:hover {
            background: #007bff;
            color: white;
            box-shadow: 0 0 20px #007bff, inset 0 0 20px #007bff;
            transform: scale(1.05);
        }

        /* --- تصميم الأيقونات المتحركة --- */
        .floating-icons {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            z-index: 1; pointer-events: none;
        }
        .floating-icons img {
            position: absolute;
            bottom: -120px;
            opacity: 0.4; /* زيادة الوضوح */
            animation: float-up 20s infinite linear;
            filter: drop-shadow(0 0 5px #4da8ff); /* إضافة توهج خفيف */
        }

        @keyframes float-up {
            0% { transform: translateY(0) rotate(0deg); opacity: 0; }
            10%, 90% { opacity: 0.4; }
            100% { transform: translateY(-110vh) rotate(360deg); opacity: 0; }
        }

        .icon1 { width: 45px; left: 5%; animation-delay: 0s; animation-duration: 25s; }
        .icon2 { width: 70px; left: 15%; animation-delay: 4s; animation-duration: 20s; }
        .icon3 { width: 50px; left: 28%; animation-delay: 8s; animation-duration: 30s; }
        .icon4 { width: 80px; left: 40%; animation-delay: 2s; animation-duration: 18s; }
        .icon5 { width: 60px; left: 55%; animation-delay: 12s; animation-duration: 28s; }
        .icon6 { width: 40px; left: 70%; animation-delay: 6s; animation-duration: 22s; }
        .icon7 { width: 75px; left: 85%; animation-delay: 1s; animation-duration: 19s; }
        .icon8 { width: 55px; left: 95%; animation-delay: 10s; animation-duration: 26s; }
        .icon9 { width: 65px; left: 20%; animation-delay: 15s; animation-duration: 24s; }
        .icon10 { width: 40px; left: 80%; animation-delay: 18s; animation-duration: 29s; }
        .icon11 { width: 70px; left: 50%; animation-delay: 9s; animation-duration: 21s; }
        .icon12 { width: 50px; left: 65%; animation-delay: 3s; animation-duration: 19s; }

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
