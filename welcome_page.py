import streamlit as st

def render_welcome_page():
    # --- استخدام حاوية لضمان عدم وجود شريط تمرير ---
    with st.container():
        # مسافات فارغة من الأعلى لدفع المحتوى للأسفل
        for _ in range(5):
            st.write("")

        # العنوان الرئيسي والنص التحفيزي
        st.markdown("<h1 style='text-align: center; color: white; font-size: 4rem; text-shadow: 0 0 10px #4da8ff;'>SIGNAL PRIME</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #cccccc; font-size: 1.5rem;'>Where Data Meets Decision.</p>", unsafe_allow_html=True)
        
        st.write("") # مسافة

        # --- عرض 6 أيقونات مضمونة في صف واحد باستخدام st.columns ---
        icon_urls = [
            "https://cryptologos.cc/logos/bitcoin-btc-logo.svg?v=025",
            "https://cryptologos.cc/logos/ethereum-eth-logo.svg?v=025",
            "https://cryptologos.cc/logos/binance-coin-bnb-logo.svg?v=025",
            "https://cryptologos.cc/logos/solana-sol-logo.svg?v=025",
            "https://cryptologos.cc/logos/cardano-ada-logo.svg?v=025",
            "https://cryptologos.cc/logos/ripple-xrp-logo.svg?v=025",
        ]
        
        # إضافة عمود فارغ على كل جانب لتوسيط الأيقونات
        _, col1, col2, col3, col4, col5, col6, _ = st.columns([1, 1, 1, 1, 1, 1, 1, 1])
        columns = [col1, col2, col3, col4, col5, col6]

        for i, col in enumerate(columns):
            with col:
                st.image(icon_urls[i], width=60)
        
        # مسافات فارغة قبل الزر
        for _ in range(4):
            st.write("")

        # --- زر البدء في المنتصف ---
        # استخدام أعمدة لتوسيط الزر
        _, center_col, _ = st.columns([1, 1.5, 1])
        with center_col:
            if st.button("🚀 Launch Scanner", use_container_width=True, key="launch_scanner_guaranteed"):
                st.session_state.show_welcome_page = False
                st.rerun()
