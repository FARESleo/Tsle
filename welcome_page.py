import streamlit as st

def render_welcome_page():
    # --- HTML جديد لصفحة الترحيب الاحترافية ---
    st.markdown("""
        <div class="floating-icons">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/2048px-Bitcoin.svg.png" alt="btc">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/512px-Ethereum-icon-purple.svg.png" alt="eth">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Binance_logo.svg/1920px-Binance_logo.svg.png" alt="bnb">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e3/Cardano-Logo.png" alt="ada">
            <img src="https://upload.wikimedia.org/wikipedia/en/d/d0/Dogecoin_Logo.png" alt="doge">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Uniswap_Logo.svg/1026px-Uniswap_Logo.svg.png" alt="uni">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/MetaMask_Fox.svg/2048px-MetaMask_Fox.svg.png" alt="metamask">
        </div>

        <div class="welcome-container" style="text-align: center; margin-top: 25vh;">
            <h1 class="glowing-title">
                الماسح الذكي
            </h1>
            <p style="font-size: 1.5rem; font-weight: bold; color: white; text-shadow: 1px 1px 2px #000000;">
                تداول بذكاء! 🧠
            </p>
        </div>
    """, unsafe_allow_html=True)

    # زر الانتقال إلى التطبيق الرئيسي (يبقى كما هو)
    if st.button("🚀 ابدأ الآن!", use_container_width=True):
        st.session_state.show_welcome_page = False
        st.rerun()
