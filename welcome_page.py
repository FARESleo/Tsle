import streamlit as st

def render_welcome_page():
    # --- استخدام أعمدة لتوسيط المحتوى بالكامل ومنع التمرير ---
    _, center_col, _ = st.columns([1, 2, 1])

    with center_col:
        # مسافات فارغة من الأعلى لدفع المحتوى للأسفل قليلاً
        for _ in range(4):
            st.write("")

        # العنوان الرئيسي والنص التحفيزي
        st.markdown("<h1 style='text-align: center; color: white; font-size: 4rem; text-shadow: 0 0 15px #4da8ff;'>SIGNAL PRIME</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #cccccc; font-size: 1.5rem;'>Where Data Meets Decision.</p>", unsafe_allow_html=True)
        
        # مسافة قبل الأيقونات
        st.write("")
        st.write("")

        # --- عرض 6 أيقونات مضمونة في صف واحد باستخدام st.columns ---
        icon_urls = [
            "https://cryptologos.cc/logos/bitcoin-btc-logo.svg?v=025",
            "https://cryptologos.cc/logos/ethereum-eth-logo.svg?v=025",
            "https://cryptologos.cc/logos/binance-coin-bnb-logo.svg?v=025",
            "https://cryptologos.cc/logos/solana-sol-logo.svg?v=025",
            "https://cryptologos.cc/logos/cardano-ada-logo.svg?v=025",
            "https://cryptologos.cc/logos/ripple-xrp-logo.svg?v=025",
        ]
        
        icon_cols = st.columns(len(icon_urls))
        for i, col in enumerate(icon_cols):
            col.image(icon_urls[i], width=50)
        
        # مسافات فارغة قبل الزر
        for _ in range(4):
            st.write("")

        # --- زر البدء في المنتصف ---
        if st.button("🚀 Launch Scanner", use_container_width=True, key="launch_scanner_guaranteed"):
            st.session_state.show_welcome_page = False
            st.rerun()
