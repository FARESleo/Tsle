import streamlit as st

def render_welcome_page(authenticator):
    # --- إعادة التصميم الأصلي بالكامل ---
    st.markdown("""
        <style>
        header, footer { visibility: hidden; }
        .stApp { background-color: #0a0a0f; overflow: hidden; }
        .floating-icons { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; }
        .floating-icons img { position: absolute; bottom: -150px; opacity: 0.4; animation: float-up 25s infinite linear; }
        @keyframes float-up { to { transform: translateY(-120vh) rotate(360deg); opacity: 0; } }
        /* ... (هنا يجب وضع تنسيقات الأيقونات الـ 32) ... */
        .floating-icons img:nth-child(1)  { left: 5%; width: 80px; animation-delay: 0s; }
        .floating-icons img:nth-child(2)  { left: 15%; width: 40px; animation-delay: 5s; }
        /* ... أكمل بقية الـ 30 تنسيقًا ... */
        .floating-icons img:nth-child(32) { left: 3%; width: 40px; animation-delay: 70s; }
        @keyframes glow {
            from { text-shadow: 0 0 10px #fff, 0 0 20px #007bff, 0 0 30px #007bff; }
            to { text-shadow: 0 0 20px #fff, 0 0 35px #4da8ff, 0 0 45px #4da8ff; }
        }
        .glowing-title { font-size: 4.5rem; color: #fff; animation: glow 1.5s ease-in-out infinite alternate; }
        .subtitle { font-size: 1.5rem; color: #cccccc; margin-top: -10px; margin-bottom: 50px; }
        /* تنسيق زر الإطلاق فقط */
        .stButton>button {
            border: 2px solid #007bff; border-radius: 50px; padding: 15px 40px;
            font-size: 1.3rem; color: white; background: transparent;
            transition: all 0.3s ease-in-out; box-shadow: 0 0 15px #007bff;
            position: relative; z-index: 2;
        }
        .stButton>button:hover { background: #007bff; box-shadow: 0 0 25px #007bff, 0 0 50px #007bff; transform: scale(1.05); }
        /* تنسيق جميل لنموذج تسجيل الدخول */
        div[data-testid="stForm"] {
            background: transparent; border: 1px solid #007bff;
            box-shadow: 0 0 20px #007bff; border-radius: 10px; padding: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- عرض مكونات الصفحة ---
    # (هذا الجزء من ملفك الأصلي، اتركه كما هو)
    icons_html = "".join([f'<img src="{url}">' for url in ICON_URLS]) # ICON_URLS from your original file
    st.markdown(f'<div class="floating-icons">{icons_html}</div>', unsafe_allow_html=True)

    if 'show_login' not in st.session_state:
        st.session_state.show_login = False

    for _ in range(7):
        st.write("") 

    st.markdown("<h1 class='glowing-title' style='text-align: center; position: relative; z-index: 2;'>SIGNAL PRIME</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle' style='text-align: center; position: relative; z-index: 2;'>Where Data Meets Decision.</p>", unsafe_allow_html=True)

    _, center_col, _ = st.columns([1, 1, 1])
    with center_col:
        if st.button("🚀 Launch Scanner", use_container_width=True):
            st.session_state.show_login = True
            st.rerun()

    # --- عرض نموذج تسجيل الدخول فقط عند الضغط على الزر ---
    if st.session_state.show_login:
        st.write("")
        _, login_col, _ = st.columns([1, 1.5, 1])
        with login_col:
            authenticator.login('main')
            if st.session_state["authentication_status"] is False:
                st.error('اسم المستخدم أو كلمة المرور غير صحيحة')
