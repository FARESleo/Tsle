import streamlit as st
import pandas as pd
from math import isnan
from datetime import datetime
import requests

# --- إعدادات الاتصال بالـ Backend ---
BACKEND_URL = "https://b6697ea5-cb9e-4031-abde-ec9d90eb52d0-00-c61ufn0y915m.worf.replit.dev"

# ------------------------------------------------------------
# (جميع الدوال المساعدة الأخرى تبقى كما هي بدون أي تغيير)
# get_instruments_from_backend, get_analysis_from_backend, 
# format_price, calculate_pnl_percentages, trading_calculator_app
# ------------------------------------------------------------
@st.cache_data(ttl=3600)
def get_instruments_from_backend():
    try:
        swap_url = f"{BACKEND_URL}/instruments?instType=SWAP"
        spot_url = f"{BACKEND_URL}/instruments?instType=SPOT"
        swap_response = requests.get(swap_url, timeout=10)
        spot_response = requests.get(spot_url, timeout=10)
        swap_response.raise_for_status()
        spot_response.raise_for_status()
        swaps = swap_response.json().get("instruments", [])
        spots = spot_response.json().get("instruments", [])
        return swaps + spots
    except requests.exceptions.RequestException as e:
        st.error(f"فشل في تحميل قائمة العملات من الخادم: {e}")
        return []

def get_analysis_from_backend(instId, bar):
    try:
        api_endpoint = f"{BACKEND_URL}/analyze"
        params = {"instId": instId, "bar": bar}
        response = requests.get(api_endpoint, params=params, timeout=120)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        error_message = f"فشل الاتصال بخادم التحليل: {e}"
        if e.response:
            try:
                error_details = e.response.json().get('detail', e.response.text)
                error_message = f"حدث خطأ في الخادم: {error_details}"
            except Exception:
                error_message = f"حدث خطأ غير معروف في الخادم. Status: {e.response.status_code}"
        return {"error": error_message}

def format_price(price, decimals=None):
    if price is None or isinstance(price, (str, bool)) or isnan(price): return "N/A"
    if decimals is None:
        if price >= 1000: decimals = 2
        elif price >= 10: decimals = 3
        else: decimals = 4
    return f"{price:,.{decimals}f}"

def calculate_pnl_percentages(entry_price, take_profit, stop_loss):
    if entry_price is None or take_profit is None or stop_loss is None or entry_price == 0:
        return None, None
    
    is_long = take_profit > entry_price
    
    if is_long:
        profit_pct = ((take_profit - entry_price) / entry_price) * 100
        loss_pct = ((stop_loss - entry_price) / entry_price) * 100
    else:
        profit_pct = ((entry_price - take_profit) / entry_price) * 100
        loss_pct = ((entry_price - stop_loss) / entry_price) * 100
        
    return profit_pct, loss_pct

def trading_calculator_app():
    st.header("🧮 حاسبة التداول")
    col1, col2 = st.columns(2)
    with col1:
        entry_price = st.number_input("سعر الدخول", min_value=0.0, format="%f")
        stop_loss_price = st.number_input("سعر وقف الخسارة", min_value=0.0, format="%f")
        risk_per_trade = st.number_input("المخاطرة لكل صفقة (%)", min_value=0.01, max_value=100.0, value=1.0)
    with col2:
        account_balance = st.number_input("رصيد الحساب", min_value=0.0, value=1000.0)
        target_price = st.number_input("سعر الهدف", min_value=0.0, format="%f")
        leverage = st.slider("الرافعة المالية", 1, 100, 10)
    if st.button("احسب"):
        if entry_price > 0 and stop_loss_price > 0 and account_balance > 0 and target_price > 0:
            risk_amount = (risk_per_trade / 100) * account_balance
            if entry_price > stop_loss_price: # Long
                price_diff = entry_price - stop_loss_price
                if price_diff == 0: st.error("فرق السعر لا يمكن أن يكون صفرًا."); return
                stop_loss_pct = price_diff / entry_price
                position_size_usdt = risk_amount / stop_loss_pct
                profit_amount = ((target_price - entry_price) / entry_price) * position_size_usdt
                rr_ratio = profit_amount / risk_amount if risk_amount > 0 else 0
                st.success("نتيجة الحساب (صفقة شراء):")
                st.metric("قيمة الصفقة (USDT)", f"{position_size_usdt:,.2f} $")
                st.metric("الربح المتوقع", f"{profit_amount:,.2f} $")
                st.metric("نسبة الربح مقابل المخاطرة (R:R)", f"{rr_ratio:.2f}x")
            elif entry_price < stop_loss_price: # Short
                price_diff = stop_loss_price - entry_price
                if price_diff == 0: st.error("فرق السعر لا يمكن أن يكون صفرًا."); return
                stop_loss_pct = price_diff / entry_price
                position_size_usdt = risk_amount / stop_loss_pct
                profit_amount = ((entry_price - target_price) / entry_price) * position_size_usdt
                rr_ratio = profit_amount / risk_amount if risk_amount > 0 else 0
                st.success("نتيجة الحساب (صفقة بيع):")
                st.metric("قيمة الصفقة (USDT)", f"{position_size_usdt:,.2f} $")
                st.metric("الربح المتوقع", f"{profit_amount:,.2f} $")
                st.metric("نسبة الربح مقابل المخاطرة (R:R)", f"{rr_ratio:.2f}x")


def render_main_app():
    # --- الكود الجديد: إعادة الخلفية والتصميم ---
    st.markdown("""
        <style>
        .stApp {
            background-image: url("https://i.imgur.com/Utvjk6E.png");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .custom-card { background-color: #1e1e1e; border-radius: 10px; padding: 15px; text-align: center; margin: 10px 0; border: 1px solid #333; height: 100%; }
        .card-header { font-size: 14px; color: #bbb; margin-bottom: 5px; }
        .card-value { font-size: 24px; font-weight: bold; color: white; }
        .progress-bar-container { background-color: #333; border-radius: 5px; height: 10px; margin-top: 10px; overflow: hidden; }
        .progress-bar { height: 100%; transition: width 0.5s ease-in-out; }
        .trade-plan-card { background-color: #1e1e1e; border-radius: 10px; padding: 20px; border: 1px solid #333; margin-top: 20px; }
        .trade-plan-title { font-size: 20px; font-weight: bold; color: #007bff; margin-bottom: 15px; text-align: center; }
        .reason-card { background-color: #2a2a2a; border-radius: 8px; padding: 15px; border-left: 5px solid; margin-bottom: 20px; }
        .reason-card.bullish { border-color: #28a745; }
        .reason-card.bearish { border-color: #dc3545; }
        .reason-card.neutral { border-color: #ffc107; }
        .reason-text { font-size: 18px; color: white; }
        .stButton>button { border-radius: 50px; background-image: linear-gradient(to right, #007bff, #0056b3); color: white; font-weight: bold; border: none; }
        .stButton>button:hover { background-image: linear-gradient(to right, #0056b3, #007bff); }
        .stMetric { background-color: #1e1e1e; border-radius: 10px; padding: 10px; text-align: center; }
        .trade-plan-item-card { background-color: #2a2a2a; border-radius: 8px; padding: 15px; text-align: center; border: 1px solid #444; height: 100%; display: flex; flex-direction: column; justify-content: center; }
        .trade-plan-item-header { font-size: 15px; color: #bbb; margin-bottom: 8px; }
        .trade-plan-item-value { font-size: 22px; font-weight: bold; color: white; word-wrap: break-word; }
        .trade-plan-item-sub-value { font-size: 14px; margin-top: 5px; min-height: 20px; }
        </style>
    """, unsafe_allow_html=True)
    # --- نهاية الكود الجديد ---

    # إدارة الحالة
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = {}
    if 'analysis_triggered' not in st.session_state:
        st.session_state.analysis_triggered = False
    
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        st.markdown("<h1 style='font-size: 2.5rem; font-weight: bold; margin: 0;'>🧠 Smart Money Scanner</h1>", unsafe_allow_html=True)
    with col2:
        if st.button("رجوع إلى الخلف ↩️"):
            st.session_state.show_welcome_page = True
            st.session_state.analysis_triggered = False # إعادة تعيين الحالة
            st.session_state.analysis_results = {}   # إعادة تعيين النتائج
            st.rerun()

    st.markdown(f"**آخر تحديث:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown("---")
    
    selected_page = st.radio("Go to", ["📊 التحليل", "🧮 الحاسبة"], horizontal=True, label_visibility="collapsed")

    if selected_page == "📊 التحليل":
        all_instruments = get_instruments_from_backend()
        if not all_instruments:
            st.error("فشل في تحميل قائمة العملات. تأكد من أن الخادم الخلفي (Backend) يعمل.")
            st.stop()
            
        selected_instId = st.selectbox("حدد الأداة", all_instruments, index=all_instruments.index("BTC-USDT-SWAP") if "BTC-USDT-SWAP" in all_instruments else 0)
        timeframes = ["15m", "30m", "1H", "4H", "6H", "12H"]
        bar = st.selectbox("الإطار الزمني", timeframes, index=2)

        if st.button("🚀 ابدأ التحليل!", use_container_width=True):
            st.session_state.analysis_triggered = True
            st.session_state.analysis_results = {}
            st.rerun()

        if st.session_state.analysis_triggered and not st.session_state.analysis_results:
            with st.spinner("...جارٍ الاتصال بالخادم وتنفيذ التحليل"):
                result = get_analysis_from_backend(selected_instId, bar)
                st.session_state.analysis_results = result
                st.session_state.analysis_triggered = False
                st.rerun()

        result = st.session_state.analysis_results

        if not result:
            st.info("💡 الرجاء تحديد أداة وإطار زمني ثم الضغط على 'ابدأ التحليل!'")
        elif 'error' in result:
            st.error(f"حدث خطأ: {result['error']}")
        elif 'recommendation' not in result:
             st.info("❌ لا توجد بيانات متاحة للعرض. قد يكون السوق هادئًا. حاول مرة أخرى لاحقًا.")
        else:
            def get_confidence_color(pct):
                if pct is None or isnan(pct): return "gray"
                if pct <= 40: return "red"
                if pct <= 60: return "orange"
                return "green"

            confidence_pct = result.get('confidence_pct', 50.0)
            confidence_color = get_confidence_color(confidence_pct)
            progress_width = confidence_pct if pd.notna(confidence_pct) else 0

            rec_emoji = "⏳"
            if result.get('recommendation') == "LONG": rec_emoji = "🚀"
            elif result.get('recommendation') == "SHORT": rec_emoji = "🔻"

            if pd.notna(confidence_pct):
                if confidence_pct >= 75: st.success("🎉 إشارة قوية تم اكتشافها!", icon="🔥")
                elif confidence_pct <= 25: st.warning("⚠️ إشارة ضعيفة. يفضل توخي الحذر.")

            # --- هذا الجزء يراه جميع المستخدمين ---
            cols = st.columns(3)
            with cols[0]:
                st.markdown(f"""<div class="custom-card"><div class="card-header">📊 الثقة</div><div class="card-value">{confidence_pct:.1f}%</div><div class="progress-bar-container"><div class="progress-bar" style="width:{progress_width}%; background-color:{confidence_color};"></div></div></div>""", unsafe_allow_html=True)
            with cols[1]:
                st.markdown(f"""<div class="custom-card"><div class="card-header">⭐ التوصية</div><div class="card-value">{rec_emoji} {result.get('recommendation', 'N/A')}</div><div style="font-size: 14px; color: #999;">({result.get('strength', 'N/A')})</div></div>""", unsafe_allow_html=True)
            with cols[2]:
                st.markdown(f"""<div class="custom-card"><div class="card-header">📈 سعر الدخول</div><div class="card-value">{format_price(result.get('entry'))}</div></div>""", unsafe_allow_html=True)

            # --- الكود الجديد: التحقق من اشتراك PRO ---
            if st.session_state.get("subscription") == "PRO":
                # --- هذا الجزء يراه فقط مشتركو PRO ---
                st.markdown("---")
                reason_text = result.get('reason', 'N/A')
                reason_class = "neutral"
                if "صعودية" in reason_text: reason_class = "bullish"
                elif "هبوطية" in reason_text: reason_class = "bearish"
                st.markdown(f"""<div class="trade-plan-card"><div class="trade-plan-title">📝 خطة التداول</div><div class="reason-card {reason_class}"><div class="trade-plan-metric-label">السبب:</div><div class="reason-text">{reason_text}</div></div>""", unsafe_allow_html=True)
                
                profit_pct, loss_pct = calculate_pnl_percentages(result.get('entry'), result.get('take_profit'), result.get('stop_loss'))
                profit_display = f"({profit_pct:+.2f}%)" if profit_pct is not None else ""
                loss_display = f"({loss_pct:.2f}%)" if loss_pct is not None else ""
                est_time_display = result.get("est_time_to_target", "")
                time_html_element = f"<br>⏱️ {est_time_display}" if est_time_display else ""
                tp_col, entry_col, sl_col = st.columns(3)
                with tp_col:
                    st.markdown(f"""<div class="trade-plan-item-card">...</div>""") # أكمل الكود من ملفك
                with entry_col:
                    st.markdown(f"""<div class="trade-plan-item-card" style="border: 2px solid #007bff;">...</div>""") # أكمل الكود من ملفك
                with sl_col:
                    st.markdown(f"""<div class="trade-plan-item-card">...</div>""") # أكمل الكود من ملفك
                
                st.markdown("---")
                st.markdown("### 📊 المقاييس الأساسية")
                # ... (كود عرض المقاييس) ...

                st.markdown("---")
                st.markdown("### 🔍 تحليل إضافي")
                # ... (كود عرض التحليل الإضافي) ...
            
            else:
                # --- رسالة للمستخدمين العاديين للترقية ---
                st.markdown("---")
                st.success("✨ للوصول إلى خطة التداول الكاملة والمقاييس المتقدمة، قم بالترقية إلى PRO!", icon="🚀")
                if st.button("الترقية إلى PRO الآن"):
                    st.balloons()
            # --- نهاية الكود الجديد ---

    elif selected_page == "🧮 الحاسبة":
        trading_calculator_app()
