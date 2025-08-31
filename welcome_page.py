# frontend/welcome_page.py
import streamlit as st

def render_welcome_page():
    # CSS خاص بصفحة الترحيب (خلفية مختلفة)
    st.markdown("""
        <style>
        .stApp {
            background-image: url("https://i.imgur.com/Ra9blqc.png");
            background-size: cover;
        }
        header, footer { visibility: hidden; }
        </style>
        """, unsafe_allow_html=True)

    # محتوى صفحة الترحيب
    st.markdown("""
        <div style="text-align: center; margin-top: 25vh;">
            <h1 style="font-size: 3rem; color: white; text-shadow: 2px 2px 4px #000000;">
                الماسح الذكي
            </h1>
            <p style="font-size: 1.5rem; font-weight: bold; color: white; text-shadow: 1px 1px 2px #000000;">
                تداول بذكاء! 🧠
            </p>
        </div>
    """, unsafe_allow_html=True)

    # زر الانتقال إلى التطبيق الرئيسي
    if st.button("🚀 ابدأ الآن!", use_container_width=True):
        st.session_state.show_welcome_page = False
        st.rerun()
