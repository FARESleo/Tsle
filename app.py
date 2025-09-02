import streamlit as st
from main_app import render_main_app
from welcome_page import render_welcome_page

st.set_page_config(
    page_title="Smart Money Scanner | SMS",
    page_icon="🧠",
    layout="wide",
)

if 'show_welcome_page' not in st.session_state:
    st.session_state.show_welcome_page = True

# --- CSS مركزي ومحسن ---
# الكود العام الذي يطبق على كل الصفحات
common_base_css = """
    header, footer { visibility: hidden; }
    .stApp {
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
"""

if st.session_state.show_welcome_page:
    # --- تصميم احترافي ومتقدم لصفحة الترحيب بخلفية دوائر متحركة ---
    
    # قائمة بروابط أيقونات عملات رقمية متنوعة
    # أضف المزيد من الروابط هنا لتظهر أيقونات أكثر
    crypto_icons = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/2048px-Bitcoin.svg.png", # BTC
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/512px-Ethereum-icon-purple.svg.png", # ETH
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Binance_logo.svg/1920px-Binance_logo.svg.png", # BNB
        "https://upload.wikimedia.org/wikipedia/e/e3/Cardano-Logo.png", # ADA
        "https://upload.wikimedia.org/wikipedia/en/d/d0/Dogecoin_Logo.png", # DOGE
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Uniswap_Logo.svg/1026px-Uniswap_Logo.svg.png", # UNI
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/MetaMask_Fox.svg/2048px-MetaMask_Fox.svg.png", # MetaMask
        "https://seeklogo.com/images/S/solana-sol-logo-D28EE9766C-seeklogo.com.png", # SOL
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Tron_logo.svg/1200px-Tron_logo.svg.png", # TRX
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Circle_USDC_Logo.png/800px-Circle_USDC_Logo.png", # USDC
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Tether_Logo.png/1200px-Tether_Logo.png", # USDT
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/XRP_Logo.svg/1200px-XRP_Logo.svg.png", # XRP
    ]

    # إنشاء عناصر img ديناميكياً بناءً على قائمة الأيقونات
    floating_icons_html = ""
    for i, icon_src in enumerate(crypto_icons):
        # لتوزيع أحجام وتأخيرات مختلفة لكل أيقونة
        size = 50 + (i % 5) * 15 # أحجام من 50px إلى 110px
        delay = (i % 7) * 4 # تأخيرات مختلفة
        duration = 20 + (i % 3) * 10 # مدة حركة مختلفة
        left_pos = 5 + (i * 7) % 90 # توزيع أفقي
        floating_icons_html += f'<img src="{icon_src}" style="left: {left_pos}%; width: {size}px; animation-delay: {delay}s; animation-duration: {duration}s;">\n'

    css = f"""
        <style>
        {common_base_css}
        .stApp {{
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460); /* خلفية متدرجة حديثة */
            background-size: cover;
        }}

        /* حاوية الأيقونات المتحركة */
        .floating-icons {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: 1;
            pointer-events: none; /* لتسمح بالضغط على العناصر خلفها */
        }}

        .floating-icons img {{
            position: absolute;
            bottom: -150px;
            opacity: 0.15;
            animation: float-up var(--duration) infinite linear;
            filter: drop-shadow(0 0 5px rgba(0, 123, 255, 0.5)); /* ظل خفيف لإبراز الأيقونات */
        }}

        /* تعريف حركة الصعود للأعلى */
        @keyframes float-up {{
            0% {{ transform: translateY(0) rotate(0deg) scale(1); opacity: 0.1; }}
            50% {{ opacity: 0.2; }}
            100% {{ transform: translateY(-120vh) rotate(360deg) scale(1.2); opacity: 0; }}
        }}

        /* تصميم العنوان الرئيسي المتوهج */
        .glowing-title {{
            font-size: 4rem;
            color: #fff;
            text-align: center;
            animation: glow 2s ease-in-out infinite alternate;
            position: relative; /* لجعله فوق الأيقونات */
            z-index: 2;
        }}
        
        /* تعريف حركة التوهج */
        @keyframes glow {{
            from {{
                text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #007bff, 0 0 40px #007bff, 0 0 50px #007bff, 0 0 60px #007bff, 0 0 70px #007bff;
            }}
            to {{
                text-shadow: 0 0 20px #fff, 0 0 30px #4da8ff, 0 0 40px #4da8ff, 0 0 50px #4da8ff, 0 0 60px #4da8ff, 0 0 70px #4da8ff, 0 0 80px #4da8ff;
            }}
        }}
        
        .welcome-container {{
            position: relative;
            z-index: 2;
            height: 100vh; /* تأكد من أن الحاوية تملأ الشاشة لتوسيط المحتوى */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
        .stButton>button {{
            position: relative;
            z-index: 3; /* لضمان أن الزر فوق كل شيء */
        }}
        </style>
    """
    # نمرر الـ HTML الخاص بالأيقونات المتحركة لصفحة الترحيب
    st.session_state.floating_icons_html = floating_icons_html

else:
    # --- CSS العادي للصفحة الرئيسية (مع إعدادات الخلفية الأصلية) ---
    background_url = "https://i.imgur.com/Utvjk6E.png"
    css = f"""
        <style>
        {common_base_css}
        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
        }}
        </style>
    """

# تطبيق الـ CSS
st.markdown(css, unsafe_allow_html=True)

# عرض الصفحة المناسبة
if st.session_state.show_welcome_page:
    render_welcome_page()
else:
    render_main_app()
