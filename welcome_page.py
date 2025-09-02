import streamlit as st

def render_welcome_page():
    # استعراض الـ HTML الخاص بالأيقونات من session_state
    floating_icons_html = st.session_state.get('floating_icons_html', '')

    st.markdown(f"""
        {floating_icons_html} <div class="welcome-container">
            <h1 class="glowing-title">
                الماسح الذكي
            </h1>
            <p style="font-size: 1.5rem; font-weight: bold; color: white; text-shadow: 1px 1px 2px #000000;">
                تداول بذكاء! 🧠
            </p>
            <div style="margin-top: 30px;">
                </div>
        </div>
    """, unsafe_allow_html=True)

    # وضع الزر خارج الـ markdown block ليتفاعل بشكل أفضل
    if st.button("🚀 ابدأ الآن!", use_container_width=True, key="start_app_button"):
        st.session_state.show_welcome_page = False
        st.rerun()
