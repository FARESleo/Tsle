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

# --- CSS مركزي ومبسط لصفحة الترحيب ---
if st.session_state.show_welcome_page:
    css = """
        <style>
        /* إخفاء العناصر الافتراضية لـ Streamlit */
        header, footer { visibility: hidden; }

        /* خلفية متدرجة داكنة وأنيقة للصفحة الأولى */
        .stApp {
            background: linear-gradient(135deg, #0a0a0f, #1a1a2e, #0a0a0f);
            background-size: cover;
            height: 100vh;
            overflow: hidden; /* لمنع أي تمرير غير مرغوب فيه */
        }

        /* حاوية المحتوى لتوسيعه وتوسيطه */
        .welcome-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh; /* تملأ كامل الارتفاع */
            text-align: center;
            position: relative;
            z-index: 2; /* لضمان ظهور المحتوى فوق الخلفية */
            padding: 20px; /* لإضافة بعض الهوامش */
            box-sizing: border-box; /* لضمان أن البادينج لا يزيد عن حجم الـ div */
        }

        /* تصميم العنوان الرئيسي المتوهج */
        .glowing-title {
            font-size: 4.5rem;
            color: #fff;
            animation: glow 1.5s ease-in-out infinite alternate;
            margin-bottom: 0.5rem; /* مسافة أسفل العنوان */
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 10px #fff, 0 0 20px #007bff, 0 0 30px #007bff; }
            to { text-shadow: 0 0 20px #fff, 0 0 35px #4da8ff, 0 0 45px #4da8ff; }
        }

        /* تصميم النص التحفيزي */
        .welcome-subtitle {
            font-size: 1.5rem;
            font-weight: bold;
            color: #cccccc;
            text-shadow: 1px 1px 2px #000000;
            margin-bottom: 3rem; /* مسافة أسفل النص التحفيزي */
        }

        /* حاوية أيقونات العملات الرقمية */
        .crypto-icons-grid {
            display: flex;
            justify-content: center;
            flex-wrap: wrap; /* للسماح للأيقونات بالانتقال إلى سطر جديد */
            gap: 20px; /* مسافة بين الأيقونات */
            margin-bottom: 4rem; /* مسافة أسفل شبكة الأيقونات */
            max-width: 90%; /* لتحديد عرض الشبكة */
        }

        .crypto-icons-grid img {
            width: 60px; /* حجم الأيقونات */
            height: 60px;
            filter: drop-shadow(0 0 8px rgba(0, 123, 255, 0.7)); /* توهج أزرق */
            transition: transform 0.3s ease-in-out; /* حركة ناعمة عند التمرير */
        }
        .crypto-icons-grid img:hover {
            transform: scale(1.2); /* تكبير عند التمرير */
        }

        /* تصميم زر البدء الاحترافي */
        .stButton>button {
            border: 2px solid #007bff;
            border-radius: 50px;
            padding: 15px 40px;
            font-size: 1.3rem;
            font-weight: bold;
            color: white;
            background: transparent;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 0 15px #007bff, inset 0 0 15px #007bff;
            cursor: pointer; /* لإظهار مؤشر اليد عند التمرير */
        }
        .stButton>button:hover {
            background: #007bff;
            color: white;
            box-shadow: 0 0 25px #007bff, inset 0 0 25px #007bff;
            transform: scale(1.05);
        }
        </style>
    """
else:
    # --- CSS العادي للصفحة الرئيسية (كما هو) ---
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
