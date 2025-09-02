import streamlit as st

def render_welcome_page():

    # قائمة أيقونات العملات الرقمية
    crypto_icons = [
        # (size, delay)
        ("80px", "0s"), ("40px", "5s"), ("60px", "10s"), ("90px", "2s"), 
        ("50px", "15s"), ("70px", "8s"), ("45px", "12s"), ("100px", "18s"),
        ("65px", "22s"), ("85px", "25s"), ("55px", "30s"), ("75px", "1s")
    ]
    
    # روابط الصور
    icon_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/2048px-Bitcoin.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Ethereum-icon-purple.svg/512px-Ethereum-icon-purple.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Binance_logo.svg/1920px-Binance_logo.svg.png",
        "https://upload.wikimedia.org/wikipedia/e/e3/Cardano-Logo.png",
        "https://upload.wikimedia.org/wikipedia/en/d/d0/Dogecoin_Logo.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Uniswap_Logo.svg/1026px-Uniswap_Logo.svg.png",
        "https://seeklogo.com/images/S/solana-sol-logo-D28EE9766C-seeklogo.com.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Tron_logo.svg/1200px-Tron_logo.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Circle_USDC_Logo.png/800px-Circle_USDC_Logo.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Tether_Logo.png/1200px-Tether_Logo.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/XRP_Logo.svg/1200px-XRP_Logo.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/MetaMask_Fox.svg/2048px-MetaMask_Fox.svg.png"
    ]

    # إنشاء عناصر img ديناميكياً
    floating_icons_html = ""
    for i in range(len(crypto_icons)):
        size, delay = crypto_icons[i]
        url = icon_urls[i % len(icon_urls)] # تكرار استخدام الصور إذا لزم الأمر
        left_pos = (i * 13) % 95 # توزيع أفقي متنوع
        floating_icons_html += f'<img src="{url}" style="--size: {size}; --delay: {delay}; left: {left_pos}%;">'
        
    # عرض كل عناصر الصفحة
    st.markdown(f"""
        <div class="background-animation">
            <div class="circle c1"></div>
            <div class="circle c2"></div>
            <div class="circle c3"></div>
            <div class="circle c4"></div>
        </div>

        <div class="floating-icons">
            {floating_icons_html}
        </div>

        <div class="welcome-container" style="text-align: center; margin-top: 25vh;">
            <h1 class="glowing-title">الماسح الذكي</h1>
            <p class="welcome-subtitle" style="font-size: 1.5rem; font-weight: bold; color: white; text-shadow: 1px 1px 2px #000000;">
                تداول بذكاء! 🧠
            </p>
        </div>
    """, unsafe_allow_html=True)

    # وضع الزر خارج الـ markdown لضمان عمله
    if st.button("🚀 ابدأ الآن!", use_container_width=True, key="start_button"):
        st.session_state.show_welcome_page = False
        st.rerun()
