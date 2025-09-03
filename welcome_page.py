import streamlit as st

# قائمة الأيقونات لتسهيل إدارتها (هذا هو الجزء المفقود)
ICON_URLS = [
    "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
    "https://assets.coingecko.com/coins/images/279/large/ethereum.png?1696501638",
    "https://assets.coingecko.com/coins/images/825/large/binance-coin-logo.png?1696502009",
    "https://assets.coingecko.com/coins/images/4128/large/solana.png?1696504756",
    "https://assets.coingecko.com/coins/images/975/large/cardano.png?1696502090",
    "https://assets.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png?1696501442",
    "https://assets.coingecko.com/coins/images/7310/large/polkadot-new-dot-logo.png?1696507567",
    "https://assets.coingecko.com/coins/images/5/large/dogecoin.png?1696501409",
    "https://assets.coingecko.com/coins/images/877/large/chainlink-new-logo.png?1696502009",
    "https://assets.coingecko.com/coins/images/13469/large/uniswap-uni.png?1696513360",
    "https://assets.coingecko.com/coins/images/2/large/litecoin.png?1696501419",
    "https://assets.coingecko.com/coins/images/325/large/Tether-logo.png?1696501661",
    "https://assets.coingecko.com/coins/images/6319/large/usdc.png?1696506694",
    "https://assets.coingecko.com/coins/images/12171/large/aave.png?1696512002",
    "https://assets.coingecko.com/coins/images/325/large/Tether.png?1696501661",
    "https://assets.coingecko.com/coins/images/11939/large/shiba.png?1696511800",
    "https://assets.coingecko.com/coins/images/12559/large/Avalanche_Circle_Red.png?1696512369",
    "https://assets.coingecko.com/coins/images/10365/large/near.png?1696510367",
    "https://assets.coingecko.com/coins/images/9576/large/BUSD.png?1696509559",
    "https://assets.coingecko.com/coins/images/1094/large/tron-logo.png?1696502193",
    "https://assets.coingecko.com/coins/images/4713/large/matic-token-icon.png?1696505277",
    "https://assets.coingecko.com/coins/images/13442/large/staked-ether.png?16965133",
    "https://assets.coingecko.com/coins/images/4529/large/Orchid-Social-Logo--Color-on-Dark.png?1696505091",
    "https://assets.coingecko.com/coins/images/12271/large/ApeCoin.png?1696512142",
    "https://assets.coingecko.com/coins/images/12817/large/filecoin.png?1696512633",
    "https://assets.coingecko.com/coins/images/9956/large/dai-multi-collateral-mcd.png?1696509959",
    "https://assets.coingecko.com/coins/images/1481/large/cosmos_hub.png?1696502525",
    "https://assets.coingecko.com/coins/images/16724/large/osmo.png?1696516388",
    "https://assets.coingecko.com/coins/images/4001/large/Fantom.png?1696504559",
    "https://assets.coingecko.com/coins/images/12645/large/A-Logo-White-Text-Black-Background-300x300.png?1696512497",
    "https://assets.coingecko.com/coins/images/24087/large/quant.png?1696523263",
    "https://assets.coingecko.com/coins/images/363/large/monero.png?1696501705",
]

def render_welcome_page(authenticator):
    # --- إعادة التصميم الأصلي بالكامل ---
    st.markdown("""
        <style>
        header, footer { visibility: hidden; }
        .stApp { background-color: #0a0a0f; overflow: hidden; }
        .floating-icons { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; }
        .floating-icons img { position: absolute; bottom: -150px; opacity: 0.4; animation: float-up 25s infinite linear; }
        @keyframes float-up { to { transform: translateY(-120vh) rotate(360deg); opacity: 0; } }
        /* ... (هنا يجب وضع تنسيقات الأيقونات الـ 32) ... */
        .floating-icons img:nth-child(1)  { left: 5%; width: 80px; animation-delay: 0s; }
        .floating-icons img:nth-child(2)  { left: 15%; width: 40px; animation-delay: 5s; }
        .floating-icons img:nth-child(3)  { left: 25%; width: 60px; animation-delay: 10s; }
        .floating-icons img:nth-child(4)  { left: 40%; width: 90px; animation-delay: 2s; }
        .floating-icons img:nth-child(5)  { left: 60%; width: 50px; animation-delay: 15s; }
        .floating-icons img:nth-child(6)  { left: 75%; width: 70px; animation-delay: 8s; }
        .floating-icons img:nth-child(7)  { left: 90%; width: 45px; animation-delay: 12s; }
        .floating-icons img:nth-child(8)  { left: 80%; width: 65px; animation-delay: 18s; }
        .floating-icons img:nth-child(9)  { left: 30%; width: 55px; animation-delay: 20s; }
        .floating-icons img:nth-child(10) { left: 70%; width: 85px; animation-delay: 25s; }
        .floating-icons img:nth-child(11) { left: 10%; width: 40px; animation-delay: 30s; }
        .floating-icons img:nth-child(12) { left: 50%; width: 70px; animation-delay: 3s; }
        .floating-icons img:nth-child(13) { left: 20%; width: 50px; animation-delay: 7s; }
        .floating-icons img:nth-child(14) { left: 85%; width: 90px; animation-delay: 11s; }
        .floating-icons img:nth-child(15) { left: 45%; width: 40px; animation-delay: 16s; }
        .floating-icons img:nth-child(16) { left: 65%; width: 75px; animation-delay: 22s; }
        .floating-icons img:nth-child(17) { left: 2%; width: 60px; animation-delay: 26s; }
        .floating-icons img:nth-child(18) { left: 35%; width: 80px; animation-delay: 29s; }
        .floating-icons img:nth-child(19) { left: 55%; width: 45px; animation-delay: 32s; }
        .floating-icons img:nth-child(20) { left: 95%; width: 65px; animation-delay: 35s; }
        .floating-icons img:nth-child(21) { left: 12%; width: 70px; animation-delay: 38s; }
        .floating-icons img:nth-child(22) { left: 28%; width: 50px; animation-delay: 42s; }
        .floating-icons img:nth-child(23) { left: 48%; width: 85px; animation-delay: 45s; }
        .floating-icons img:nth-child(24) { left: 68%; width: 40px; animation-delay: 48s; }
        .floating-icons img:nth-child(25) { left: 88%; width: 75px; animation-delay: 50s; }
        .floating-icons img:nth-child(26) { left: 8%; width: 55px; animation-delay: 53s; }
        .floating-icons img:nth-child(27) { left: 22%; width: 90px; animation-delay: 56s; }
        .floating-icons img:nth-child(28) { left: 42%; width: 45px; animation-delay: 59s; }
        .floating-icons img:nth-child(29) { left: 62%; width: 80px; animation-delay: 62s; }
        .floating-icons img:nth-child(30) { left: 78%; width: 50px; animation-delay: 65s; }
        .floating-icons img:nth-child(31) { left: 92%; width: 70px; animation-delay: 68s; }
        .floating-icons img:nth-child(32) { left: 3%; width: 40px; animation-delay: 70s; }
        @keyframes glow {
            from { text-shadow: 0 0 10px #fff, 0 0 20px #007bff, 0 0 30px #007bff; }
            to { text-shadow: 0 0 20px #fff, 0 0 35px #4da8ff, 0 0 45px #4da8ff; }
        }
        .glowing-title { font-size: 4.5rem; color: #fff; animation: glow 1.5s ease-in-out infinite alternate; }
        .subtitle { font-size: 1.5rem; color: #cccccc; margin-top: -10px; margin-bottom: 50px; }
        /* تنسيق زر الإطلاق فقط */
        .stButton>button {
            border: 2px solid #007bff; border-radius: 50px; padding: 15px 40px;
            font-size: 1.3rem; color: white; background: transparent;
            transition: all 0.3s ease-in-out; box-shadow: 0 0 15px #007bff;
            position: relative; z-index: 2;
        }
        .stButton>button:hover { background: #007bff; box-shadow: 0 0 25px #007bff, 0 0 50px #007bff; transform: scale(1.05); }
        /* تنسيق جميل لنموذج تسجيل الدخول */
        div[data-testid="stForm"] {
            background: transparent; border: 1px solid #007bff;
            box-shadow: 0 0 20px #007bff; border-radius: 10px; padding: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- عرض مكونات الصفحة ---
    icons_html = "".join([f'<img src="{url}">' for url in ICON_URLS])
    st.markdown(f'<div class="floating-icons">{icons_html}</div>', unsafe_allow_html=True)

    if 'show_login' not in st.session_state:
        st.session_state.show_login = False

    for _ in range(7):
        st.write("") 

    st.markdown("<h1 class='glowing-title' style='text-align: center; position: relative; z-index: 2;'>SIGNAL PRIME</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle' style='text-align: center; position: relative; z-index: 2;'>Where Data Meets Decision.</p>", unsafe_allow_html=True)

    _, center_col, _ = st.columns([1, 1, 1])
    with center_col:
        if st.button("🚀 Launch Scanner", use_container_width=True):
            st.session_state.show_login = True
            st.rerun()

    # --- عرض نموذج تسجيل الدخول فقط عند الضغط على الزر ---
    if st.session_state.show_login:
        st.write("")
        _, login_col, _ = st.columns([1, 1.5, 1])
        with login_col:
            authenticator.login('main')
            if st.session_state["authentication_status"] is False:
                st.error('اسم المستخدم أو كلمة المرور غير صحيحة')
