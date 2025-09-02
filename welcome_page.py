import streamlit as st

def render_welcome_page():
    
    st.markdown("""
        <div class="stars"></div>
        <div class="twinkling"></div>

        <div class="floating-icons">
            <img class="icon1" src="https://www.svgrepo.com/show/303423/bitcoin-btc-logo.svg">
            <img class="icon2" src="https://www.svgrepo.com/show/303388/ethereum-eth-logo.svg">
            <img class="icon3" src="https://www.svgrepo.com/show/303414/binance-coin-bnb-logo.svg">
            <img class="icon4" src="https://www.svgrepo.com/show/428678/solana-sol.svg">
            <img class="icon5" src="https://www.svgrepo.com/show/303683/dogecoin-doge-logo.svg">
            <img class="icon6" src="https://www.svgrepo.com/show/303509/tether-usdt-logo.svg">
            <img class="icon7" src="https://www.svgrepo.com/show/303632/xrp-xrp-logo.svg">
            <img class="icon8" src="https://www.svgrepo.com/show/303442/cardano-ada-logo.svg">
            <img class="icon9" src="https://www.svgrepo.com/show/303496/chainlink-link-logo.svg">
            <img class="icon10" src="https://www.svgrepo.com/show/303601/uniswap-uni-logo.svg">
            <img class="icon11" src="https://www.svgrepo.com/show/303487/litecoin-ltc-logo.svg">
            <img class="icon12" src="https://www.svgrepo.com/show/303565/polkadot-new-dot-logo.svg">
        </div>

        <div class="welcome-container">
            <h1 class="glowing-title">Signal Prime</h1>
            <p style="font-size: 1.5rem; font-weight: bold; color: #cccccc; text-shadow: 1px 1px 2px #000000;">
                Where Data Meets Decision.
            </p>
            <div style="margin-top: 40px;"></div>
        </div>
    """, unsafe_allow_html=True)

    # وضع الزر خارج الـ markdown لضمان عمله وتطبيق التصميم الجديد
    if st.button("🚀 Launch Scanner", use_container_width=False, key="launch_button"):
        st.session_state.show_welcome_page = False
        st.rerun()
