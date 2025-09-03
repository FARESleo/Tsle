import streamlit as st

# قائمة الأيقونات لتسهيل إدارتها
ICON_URLS = [
    "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
    "https://assets.coingecko.com/coins/images/279/large/ethereum.png?1696501638",
    "https://assets.coingecko.com/coins/images/825/large/binance-coin-logo.png?1696502009",
    "https://assets.coingecko.com/coins/images/4128/large/solana.png?1696504756",
    "https://assets.coingecko.com/coins/images/975/large/cardano.png?1696502090",
    "https://assets.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png?1696501442",
    "https://assets.coingecko.com/coins/images/7310/large/polkadot-new-dot-logo.png?1696507567",
    "https://assets.coingecko.com/coins/images/5/large/dogecoin.png?1696501409",
    "https://assets.coingecko.com/coins/images/877/large/chainlink-new-logo.png?1696502009",
    "https://assets.coingecko.com/coins/images/13469/large/uniswap-uni.png?1696513360",
    "https://assets.coingecko.com/coins/images/2/large/litecoin.png?1696501419",
    "https://assets.coingecko.com/coins/images/325/large/Tether-logo.png?1696501661",
    "https://assets.coingecko.com/coins/images/6319/large/usdc.png?1696506694",
    "https://assets.coingecko.com/coins/images/12171/large/aave.png?1696512002",
    "https://assets.coingecko.com/coins/images/325/large/Tether.png?1696501661",
    "https://assets.coingecko.com/coins/images/11939/large/shiba.png?1696511800",
    "https://assets.coingecko.com/coins/images/12559/large/Avalanche_Circle_Red.png?1696512369",
    "https://assets.coingecko.com/coins/images/10365/large/near.png?1696510367",
    "https://assets.coingecko.com/coins/images/9576/large/BUSD.png?1696509559",
    "https://assets.coingecko.com/coins/images/1094/large/tron-logo.png?1696502193",
    "https://assets.coingecko.com/coins/images/4713/large/matic-token-icon.png?1696505277",
    "https://assets.coingecko.com/coins/images/13442/large/staked-ether.png?16965133",
    "https://assets.coingecko.com/coins/images/4529/large/Orchid-Social-Logo--Color-on-Dark.png?1696505091",
    "https://assets.coingecko.com/coins/images/12271/large/ApeCoin.png?1696512142",
    "https://assets.coingecko.com/coins/images/12817/large/filecoin.png?1696512633",
    "https://assets.coingecko.com/coins/images/9956/large/dai-multi-collateral-mcd.png?1696509959",
    "https://assets.coingecko.com/coins/images/1481/large/cosmos_hub.png?1696502525",
    "https://assets.coingecko.com/coins/images/16724/large/osmo.png?1696516388",
    "https://assets.coingecko.com/coins/images/4001/large/Fantom.png?1696504559",
    "https://assets.coingecko.com/coins/images/12645/large/A-Logo-White-Text-Black-Background-300x300.png?1696512497",
    "https://assets.coingecko.com/coins/images/24087/large/quant.png?1696523263",
    "https://assets.coingecko.com/coins/images/363/large/monero.png?1696501705",
]

def render_welcome_page():
    # إنشاء HTML للأيقونات العائمة من القائمة
    icons_html = "".join([f'<img src="{url}">' for url in ICON_URLS])
    st.markdown(f'<div class="floating-icons">{icons_html}</div>', unsafe_allow_html=True)

    # محتوى الصفحة
    for _ in range(7):
        st.write("")

    st.markdown("<h1 class='glowing-title' style='text-align: center; position: relative; z-index: 2;'>SIGNAL PRIME</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle' style='text-align: center; position: relative; z-index: 2;'>Where Data Meets Decision.</p>", unsafe_allow_html=True)

    _, center_col, _ = st.columns([1, 1, 1])
    with center_col:
        if st.button("🚀 Launch Scanner", use_container_width=True, key="launch_scanner"):
            st.session_state.show_welcome_page = False
            st.rerun()
