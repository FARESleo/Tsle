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
        
        /* --- الأيقونات العائمة بالحركة العشوائية --- */
        .floating-icons {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            z-index: 1; pointer-events: none;
        }
        .floating-icons img {
            position: absolute;
            bottom: -150px; /* ابدأ من خارج الشاشة */
            opacity: 0.2; /* زيادة الوضوح */
            animation: float-up 25s infinite linear;
        }
        @keyframes float-up {
            to { transform: translateY(-120vh) rotate(360deg); opacity: 0; }
        }
        
        /* (هذا هو الجزء الأهم) أحجام ومواقع وتأخيرات وسرعات مختلفة لكل أيقونة */
        .floating-icons img:nth-child(1) { left: 5%; width: 80px; animation-delay: 0s; }
        .floating-icons img:nth-child(2) { left: 15%; width: 40px; animation-delay: 5s; animation-duration: 30s; }
        .floating-icons img:nth-child(3) { left: 25%; width: 60px; animation-delay: 10s; }
        .floating-icons img:nth-child(4) { left: 40%; width: 90px; animation-delay: 2s; animation-duration: 20s; }
        .floating-icons img:nth-child(5) { left: 60%; width: 50px; animation-delay: 15s; }
        .floating-icons img:nth-child(6) { left: 75%; width: 70px; animation-delay: 8s; animation-duration: 35s; }
        .floating-icons img:nth-child(7) { left: 90%; width: 45px; animation-delay: 12s; }
        .floating-icons img:nth-child(8) { left: 80%; width: 65px; animation-delay: 18s; animation-duration: 22s; }
        .floating-icons img:nth-child(9) { left: 30%; width: 55px; animation-delay: 20s; }
        .floating-icons img:nth-child(10) { left: 70%; width: 85px; animation-delay: 25s; animation-duration: 18s; }
        .floating-icons img:nth-child(11) { left: 10%; width: 40px; animation-delay: 30s; animation-duration: 40s; }
        .floating-icons img:nth-child(12) { left: 50%; width: 70px; animation-delay: 3s; animation-duration: 25s; }

        /* --- تصميم النصوص والزر --- */
        /* (هذا هو التوهج الذي تريده) */
        @keyframes glow {
            from { text-shadow: 0 0 10px #fff, 0 0 20px #007bff, 0 0 30px #007bff; }
            to { text-shadow: 0 0 20px #fff, 0 0 35px #4da8ff, 0 0 45px #4da8ff; }
        }
        .glowing-title {
            font-size: 4.5rem;
            color: #fff;
            animation: glow 1.5s ease-in-out infinite alternate;
        }
        .subtitle {
            font-size: 1.5rem;
            color: #cccccc;
            margin-top: -10px;
            margin-bottom: 50px;
        }
        .stButton>button {
            border: 2px solid #007bff; border-radius: 50px; padding: 15px 40px;
            font-size: 1.3rem; color: white; background: transparent;
            transition: all 0.3s ease-in-out; box-shadow: 0 0 15px #007bff;
            position: relative; z-index: 2;
        }
        .stButton>button:hover {
            background: #007bff; box-shadow: 0 0 25px #007bff, 0 0 50px #007bff;
            transform: scale(1.05);
        }
        </style>

        <div class="floating-icons">
            <img src="https://www.svgrepo.com/show/303423/bitcoin-btc-logo.svg">
            <img src="https://www.svgrepo.com/show/303388/ethereum-eth-logo.svg">
            <img src="https://www.svgrepo.com/show/303414/binance-coin-bnb-logo.svg">
            <img src="https://www.svgrepo.com/show/428678/solana-sol.svg">
            <img src="https://www.svgrepo.com/show/303442/cardano-ada-logo.svg">
            <img src="https://www.svgrepo.com/show/303632/xrp-xrp-logo.svg">
            <img src="https://www.svgrepo.com/show/303565/polkadot-new-dot-logo.svg">
            <img src="https://www.svgrepo.com/show/303683/dogecoin-doge-logo.svg">
            <img src="https://www.svgrepo.com/show/303496/chainlink-link-logo.svg">
            <img src="https://www.svgrepo.com/show/303601/uniswap-uni-logo.svg">
            <img src="https://www.svgrepo.com/show/303487/litecoin-ltc-logo.svg">
            <img src="https://www.svgrepo.com/show/303509/tether-usdt-logo.svg">
        </div>
    """, unsafe_allow_html=True)

    # --- استخدام مكونات Streamlit للتحكم في مكان المحتوى (هذا يحل مشكلة التمرير) ---
    for _ in range(7):
        st.write("") # مسافات فارغة من الأعلى

    st.markdown("<h1 class='glowing-title' style='text-align: center; position: relative; z-index: 2;'>SIGNAL PRIME</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle' style='text-align: center; position: relative; z-index: 2;'>Where Data Meets Decision.</p>", unsafe_allow_html=True)

    # استخدام أعمدة لتوسيط الزر
    _, center_col, _ = st.columns([1, 1, 1])
    with center_col:
        if st.button("🚀 Launch Scanner", use_container_width=True, key="launch_scanner_the_one"):
            st.session_state.show_welcome_page = False
            st.rerun()
