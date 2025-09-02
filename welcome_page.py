import streamlit as st

def render_welcome_page():
    # --- هذا الكود يحتوي على كل شيء: التصميم، المحتوى، والأيقونات العائمة ---
    st.markdown("""
        <style>
        /* إخفاء العناصر الافتراضية */
        header, footer { visibility: hidden; }
        .stApp {
            background-color: #0a0a0f; /* خلفية داكنة وأنيقة */
            overflow: hidden; /* منع التمرير نهائياً */
        }
        
        /* --- الأيقونات العائمة --- */
        .floating-icons {
            position: fixed; /* استخدم fixed بدلاً من absolute */
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1; /* اجعل الأيقونات في الخلف */
            pointer-events: none; /* للسماح بالضغط على الزر */
        }
        .floating-icons img {
            position: absolute;
            bottom: -100px;
            opacity: 0.15; /* زيادة الوضوح قليلاً */
            animation: float-up 20s infinite linear;
        }
        @keyframes float-up {
            to {
                transform: translateY(-110vh) rotate(360deg);
                opacity: 0;
            }
        }
        /* أحجام ومواقع وتأخيرات مختلفة لكل أيقونة */
        .icon1 { width: 45px; left: 5%; animation-delay: 0s; animation-duration: 25s; }
        .icon2 { width: 70px; left: 15%; animation-delay: 4s; animation-duration: 20s; }
        .icon3 { width: 50px; left: 28%; animation-delay: 8s; animation-duration: 30s; }
        .icon4 { width: 80px; left: 40%; animation-delay: 2s; animation-duration: 18s; }
        .icon5 { width: 60px; left: 55%; animation-delay: 12s; animation-duration: 28s; }
        .icon6 { width: 40px; left: 70%; animation-delay: 6s; animation-duration: 22s; }
        .icon7 { width: 75px; left: 85%; animation-delay: 1s; animation-duration: 19s; }
        .icon8 { width: 55px; left: 95%; animation-delay: 10s; animation-duration: 26s; }

        /* --- تصميم الزر --- */
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
            position: relative; /* مهم ليعمل الزر فوق طبقة الأيقونات */
            z-index: 2;
        }
        .stButton>button:hover {
            background: #007bff;
            box-shadow: 0 0 25px #007bff, 0 0 50px #007bff;
            transform: scale(1.05);
        }
        </style>

        <div class="floating-icons">
            <img class="icon1" src="https://cryptologos.cc/logos/bitcoin-btc-logo.svg?v=025">
            <img class="icon2" src="https://cryptologos.cc/logos/ethereum-eth-logo.svg?v=025">
            <img class="icon3" src="https://cryptologos.cc/logos/binance-coin-bnb-logo.svg?v=025">
            <img class="icon4" src="https://cryptologos.cc/logos/solana-sol-logo.svg?v=025">
            <img class="icon5" src="https://cryptologos.cc/logos/cardano-ada-logo.svg?v=025">
            <img class="icon6" src="https://cryptologos.cc/logos/ripple-xrp-logo.svg?v=025">
            <img class="icon7" src="https://cryptologos.cc/logos/polkadot-dot-logo.svg?v=025">
            <img class="icon8" src="https://cryptologos.cc/logos/dogecoin-doge-logo.svg?v=025">
        </div>
    """, unsafe_allow_html=True)

    # --- استخدام مكونات Streamlit للتحكم في مكان المحتوى (هذا يحل مشكلة التمرير) ---
    # مسافات فارغة من الأعلى لدفع المحتوى للأسفل
    for _ in range(7):
        st.write("")

    # العنوان الرئيسي والنص التحفيزي
    st.markdown("<h1 style='text-align: center; color: white; font-size: 4.5rem; text-shadow: 0 0 15px rgba(0, 123, 255, 0.7); position: relative; z-index: 2;'>SIGNAL PRIME</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #cccccc; font-size: 1.5rem; margin-top: -10px; margin-bottom: 50px; position: relative; z-index: 2;'>Where Data Meets Decision.</p>", unsafe_allow_html=True)

    # استخدام أعمدة لتوسيط الزر
    _, center_col, _ = st.columns([1, 1, 1])
    with center_col:
        if st.button("🚀 Launch Scanner", use_container_width=True, key="launch_scanner_final_final"):
            st.session_state.show_welcome_page = False
            st.rerun()
