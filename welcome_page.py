import streamlit as st

def render_welcome_page():
    
    # روابط أيقونات عالية الجودة ومضمونة
    icon_urls = [
        "https://cryptologos.cc/logos/bitcoin-btc-logo.svg?v=025",
        "https://cryptologos.cc/logos/ethereum-eth-logo.svg?v=025",
        "https://cryptologos.cc/logos/binance-coin-bnb-logo.svg?v=025",
        "https://cryptologos.cc/logos/solana-sol-logo.svg?v=025",
        "https://cryptologos.cc/logos/cardano-ada-logo.svg?v=025",
        "https://cryptologos.cc/logos/ripple-xrp-logo.svg?v=025",
        "https://cryptologos.cc/logos/polkadot-dot-logo.svg?v=025",
    ]

    # بناء HTML لصف الأيقونات
    icons_html = "".join([f'<img src="{url}" alt="Crypto Icon">' for url in icon_urls])

    st.markdown(f"""
        <div class="welcome-container">
            
            <h1 class="glowing-title">SIGNAL PRIME</h1>
            
            <p class="welcome-subtitle">Your Edge in the Crypto Market. Unleash Smart Insights.</p>
            
            <div class="crypto-icons-row">
                {icons_html}
            </div>
            
        </div>
    """, unsafe_allow_html=True)

    # وضع الزر خارج الـ markdown لضمان عمله
    if st.button("🚀 Launch Scanner", use_container_width=False, key="final_launch_button"):
        st.session_state.show_welcome_page = False
        st.rerun()
