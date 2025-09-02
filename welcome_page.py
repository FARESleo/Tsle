import streamlit as st

def render_welcome_page():
    # --- هذا الكود يحتوي على كل شيء: التصميم والمحتوى والزر ---
    st.markdown("""
        <style>
        /* إخفاء العناصر الافتراضية */
        header, footer { visibility: hidden; }
        .stApp {
            background-color: #0a0a0f; /* خلفية داكنة وأنيقة */
            overflow: hidden; /* منع التمرير */
        }
        /* حاوية لتوسيط كل شيء في الصفحة */
        .welcome-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        /* تصميم العنوان الرئيسي */
        .main-title {
            font-size: 5rem;
            color: #ffffff;
            font-weight: 700;
            letter-spacing: 2px;
            text-shadow: 0 0 15px rgba(0, 123, 255, 0.7);
        }
        /* تصميم النص التحفيزي */
        .subtitle {
            font-size: 1.5rem;
            color: #cccccc;
            margin-top: -10px;
            margin-bottom: 50px; /* مسافة بين النص والزر */
        }
        /* تصميم الزر */
        .stButton>button {
            border: 2px solid #007bff;
            border-radius: 50px;
            padding: 15px 40px;
            font-size: 1.3rem;
            font-weight: bold;
            color: white;
            background: transparent;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 0 15px #007bff;
        }
        .stButton>button:hover {
            background: #007bff;
            box-shadow: 0 0 25px #007bff, 0 0 50px #007bff;
            transform: scale(1.05);
        }
        </style>

        <div class="welcome-container">
            <h1 class="main-title">SIGNAL PRIME</h1>
            <p class="subtitle">Where Data Meets Decision.</p>
        </div>
    """, unsafe_allow_html=True)

    # وضع الزر في حاوية منفصلة لضمان عمله
    with st.container():
        # استخدام أعمدة لتوسيط الزر
        _, center_col, _ = st.columns([1, 1, 1])
        with center_col:
            if st.button("🚀 Launch Scanner", use_container_width=True, key="launch_scanner_final_stable"):
                st.session_state.show_welcome_page = False
                st.rerun()
