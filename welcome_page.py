import streamlit as st

def render_welcome_page():
    # --- استخدام حاوية لتوسيط المحتوى ---
    with st.container():
        # مسافة فارغة من الأعلى لدفع المحتوى للأسفل
        st.write("")
        st.write("")

        # العنوان الرئيسي والنص التحفيزي
        st.markdown("""
            <h1 style='text-align: center; color: white; font-size: 4rem;'>SIGNAL PRIME</h1>
            <p style='text-align: center; color: #cccccc; font-size: 1.5rem;'>Your Edge in the Crypto Market. Unleash Smart Insights.</p>
        """, unsafe_allow_html=True)

        st.write("") # مسافة
        
        # --- عرض أيقونات العملات الرقمية باستخدام st.columns لضمان الترتيب الصحيح ---
        icon_urls = [
            "https://cryptologos.cc/logos/bitcoin-btc-logo.svg?v=025",
            "https://cryptologos.cc/logos/ethereum-eth-logo.svg?v=025",
            "https://cryptologos.cc/logos/binance-coin-bnb-logo.svg?v=025",
            "https://cryptologos.cc/logos/solana-sol-logo.svg?v=025",
            "https://cryptologos.cc/logos/cardano-ada-logo.svg?v=025",
            "https://cryptologos.cc/logos/ripple-xrp-logo.svg?v=025",
        ]
        
        # إنشاء 6 أعمدة لعرض الأيقونات
        cols = st.columns(len(icon_urls))
        for i, col in enumerate(cols):
            with col:
                st.image(icon_urls[i], width=60)

        st.write("") # مسافة
        st.write("") # مسافة

        # --- زر البدء ---
        # استخدام أعمدة لتوسيط الزر
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🚀 Launch Scanner", use_container_width=True, key="launch_scanner_final"):
                st.session_state.show_welcome_page = False
                st.rerun()
