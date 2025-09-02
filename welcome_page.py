import streamlit as st

def render_welcome_page():
    
    # قائمة بأيقونات العملات الرقمية ذات روابط موثوقة وعالية الجودة
    # تم اختيار هذه الروابط بعناية لضمان عملها وظهور الأيقونات بشكل صحيح
    icon_urls = [
        "https://cryptologos.cc/logos/bitcoin-btc-logo.svg?v=025",
        "https://cryptologos.cc/logos/ethereum-eth-logo.svg?v=025",
        "https://cryptologos.cc/logos/binance-coin-bnb-logo.svg?v=025",
        "https://cryptologos.cc/logos/solana-sol-logo.svg?v=025",
        "https://cryptologos.cc/logos/cardano-ada-logo.svg?v=025",
        "https://cryptologos.cc/logos/ripple-xrp-logo.svg?v=025",
        "https://cryptologos.cc/logos/polkadot-dot-logo.svg?v=025",
        "https://cryptologos.cc/logos/dogecoin-doge-logo.svg?v=025",
        "https://cryptologos.cc/logos/chainlink-link-logo.svg?v=025",
        "https://cryptologos.cc/logos/uniswap-uni-logo.svg?v=025",
        "https://cryptologos.cc/logos/litecoin-ltc-logo.svg?v=025",
        "https://cryptologos.cc/logos/tether-usdt-logo.svg?v=025",
        "https://cryptologos.cc/logos/usd-coin-usdc-logo.svg?v=025",
        "https://cryptologos.cc/logos/avalanche-avax-logo.svg?v=025",
        "https://cryptologos.cc/logos/tron-trx-logo.svg?v=025",
        "https://cryptologos.cc/logos/shiba-inu-shib-logo.svg?v=025",
    ]

    # بناء HTML لشبكة الأيقونات
    icons_html = "".join([f'<img src="{url}" alt="Crypto Icon">' for url in icon_urls])

    st.markdown(f"""
        <div class="welcome-container">
            <h1 class="glowing-title">SIGNAL PRIME</h1>
            <p class="welcome-subtitle">Your Edge in the Crypto Market. Unleash Smart Insights.</p>
            
            <div class="crypto-icons-grid">
                {icons_html}
            </div>
            
        </div>
    """, unsafe_allow_html=True)

    # وضع الزر خارج الـ markdown لضمان عمله وتطبيق التصميم الجديد
    if st.button("🚀 Launch Scanner", use_container_width=False, key="launch_button_final"):
        st.session_state.show_welcome_page = False
        st.rerun()
