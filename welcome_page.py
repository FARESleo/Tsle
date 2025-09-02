import streamlit as st

def render_welcome_page():
    
    st.markdown("""
        <div class="floating-icons">
            <img class="icon1" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/2048px-Bitcoin.svg.png">
            <img class="icon2" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/512px-Ethereum-icon-purple.svg.png">
            <img class="icon3" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Binance_logo.svg/1920px-Binance_logo.svg.png">
            <img class="icon4" src="https://seeklogo.com/images/S/solana-sol-logo-D28EE9766C-seeklogo.com.png">
            <img class="icon5" src="https://upload.wikimedia.org/wikipedia/en/d/d0/Dogecoin_Logo.png">
            <img class="icon6" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Tether_Logo.png/1200px-Tether_Logo.png">
            <img class="icon7" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/XRP_Logo.svg/1200px-XRP_Logo.svg.png">
            <img class="icon8" src="https://upload.wikimedia.org/wikipedia/e/e3/Cardano-Logo.png">
        </div>

        <div class="welcome-container">
            <h1 class="glowing-title">الماسح الذكي</h1>
            <p style="font-size: 1.5rem; font-weight: bold; color: white; text-shadow: 1px 1px 2px #000000;">
                تداول بذكاء! 🧠
            </p>
        </div>
    """, unsafe_allow_html=True)

    # وضع الزر خارج الـ markdown لضمان عمله
    if st.button("🚀 ابدأ الآن!", use_container_width=True, key="start_button_final"):
        st.session_state.show_welcome_page = False
        st.rerun()
