# main_app.py (إصدار العميل الذكي - يتصل بالـ Backend API)
import streamlit as st
import pandas as pd
from math import isnan
from datetime import datetime
import requests # <-- المكتبة الأساسية للاتصال بالـ Backend

# --- إعدادات الاتصال بالـ Backend ---
# !!! هام جداً: استبدل هذا الرابط بالرابط العام لمشروعك على Replit
BACKEND_URL = "https://b6697ea5-cb9e-4031-abde-ec9d90eb52d0-00-c61ufn0y915m.worf.replit.dev"

# ------------------------------------------------------------
# دوال مساعدة للتواصل مع الـ Backend API
# ------------------------------------------------------------

@st.cache_data(ttl=3600) # كاش لمدة ساعة لقائمة العملات لأنها لا تتغير كثيراً
def get_instruments_from_backend():
    """تجلب قائمة أدوات التداول من الـ Backend."""
    try:
        # نفترض أن الـ backend يوفر نقطة نهاية (endpoint) لجلب الأدوات
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

@st.cache_data(ttl=60) # كاش لمدة دقيقة لبيانات السوق
def get_market_data_from_backend():
    """تجلب بيانات السوق اللحظية من الـ Backend."""
    try:
        # نفترض أن الـ backend يوفر نقطة نهاية لبيانات CoinGecko
        response = requests.get(f"{BACKEND_URL}/market_data", timeout=15)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        st.error(f"فشل في جلب بيانات السوق من الخادم: {e}")
        return pd.DataFrame()

def get_analysis_from_backend(instId, bar):
    """
    يرسل طلب تحليل إلى الـ Backend ويستلم النتيجة.
    لا نستخدم الكاش هنا لأننا نريد تحليلًا جديدًا في كل مرة نضغط فيها على الزر.
    """
    try:
        api_endpoint = f"{BACKEND_URL}/analyze"
        params = {"instId": instId, "bar": bar}
        response = requests.get(api_endpoint, params=params, timeout=120) # مهلة طويلة للتحليل
        response.raise_for_status() # سيؤدي إلى خطأ إذا كانت الاستجابة 4xx or 5xx
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

# ------------------------------------------------------------
# دوال الواجهة (تبقى كما هي تقريباً)
# ------------------------------------------------------------
def format_price(price, decimals=None):
    if price is None or isinstance(price, (str, bool)) or isnan(price): return "N/A"
    if decimals is None:
        if price >= 1000: decimals = 2
        elif price >= 10: decimals = 3
        else: decimals = 4
    return f"{price:,.{decimals}f}"

def calculate_pnl_percentages(entry_price, take_profit, stop_loss):
    if entry_price is None or take_profit is None or stop_loss is None or entry_price == 0: return None, None
    profit_pct = ((take_profit - entry_price) / entry_price) * 100
    loss_pct = ((stop_loss - entry_price) / entry_price) * 100
    is_long = take_profit > entry_price
    if not is_long: profit_pct, loss_pct = loss_pct, profit_pct
    return profit_pct, loss_pct

def trading_calculator_app():
    # ... (هذه الدالة تبقى كما هي بدون تغيير)
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

def live_market_tracker():
    st.header("📊 متتبع السوق اللحظي")
    # <-- تغيير: استدعاء الدالة الجديدة التي تتصل بالـ Backend
    df = get_market_data_from_backend()
    if not df.empty:
        st.dataframe(df.rename(columns={
            "name": "الاسم", "symbol": "الرمز", "current_price": "السعر الحالي",
            "price_change_percentage_24h": "تغيير 24 ساعة", "high_24h": "أعلى سعر 24 ساعة",
            "low_24h": "أدنى سعر 24 ساعة"
        }))
    else:
        st.warning("لا يمكن عرض بيانات السوق حالياً. يرجى المحاولة لاحقاً.")

def render_main_app():
    st.set_page_config(layout="wide")
    
    # ... (CSS يبقى كما هو)
    st.markdown("""<style>...</style>""", unsafe_allow_html=True)
    
    if 'analysis_results' not in st.session_state: st.session_state.analysis_results = {}
    if 'last_instId' not in st.session_state: st.session_state.last_instId = ""
    if 'last_bar' not in st.session_state: st.session_state.last_bar = ""
    
    st.markdown("<h1 style='font-size: 2.5rem; font-weight: bold; margin: 0;'>🧠 Smart Money Scanner</h1>", unsafe_allow_html=True)
    st.markdown(f"**آخر تحديث:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown("---")
    
    selected_page = st.radio("Go to", ["📊 التحليل", "🧮 الحاسبة", "📈 المتتبع"], horizontal=True, label_visibility="collapsed")

    if selected_page == "📊 التحليل":
        # <-- تغيير: استدعاء الدالة الجديدة لجلب قائمة العملات من الـ Backend
        all_instruments = get_instruments_from_backend()
        
        if not all_instruments:
            st.error("فشل في تحميل قائمة العملات. تأكد من أن الخادم الخلفي (Backend) يعمل.")
            st.stop()
            
        selected_instId = st.selectbox("حدد الأداة", all_instruments, index=all_instruments.index("BTC-USDT-SWAP") if "BTC-USDT-SWAP" in all_instruments else 0)
        timeframes = ["15m", "30m", "1H", "4H", "6H", "12H"]
        bar = st.selectbox("الإطار الزمني", timeframes, index=2)

        # ... (منطق st.session_state يبقى كما هو)

        if st.button("🚀 ابدأ التحليل!", use_container_width=True):
            st.session_state.analysis_in_progress = True
            
        if st.session_state.get('analysis_in_progress', False):
            with st.spinner("...جارٍ الاتصال بالخادم وتنفيذ التحليل"):
                # <-- تغيير جذري: استدعاء دالة واحدة فقط تتصل بالـ Backend
                result = get_analysis_from_backend(selected_instId, bar)
                st.session_state.analysis_results = result
                st.session_state.analysis_in_progress = False
        
        result = st.session_state.analysis_results

        # ... (باقي الكود الخاص بعرض النتائج يبقى كما هو تماماً)
        if not isinstance(result, dict) or not result:
            st.info("💡 الرجاء تحديد أداة وإطار زمني ثم الضغط على 'ابدأ التحليل!'")
        elif 'error' in result:
            st.error(f"حدث خطأ: {result['error']}")
        elif 'recommendation' not in result:
             st.info("❌ لا توجد بيانات متاحة للعرض. الرجاء الضغط 'ابدأ التحليل!'")
        else:
            # ... (كل الكود الخاص بعرض البطاقات والرسوم البيانية يبقى هنا)
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
            cols = st.columns(3)
            with cols[0]:
                st.markdown(f"""<div class="custom-card"><div class="card-header">📊 الثقة</div><div class="card-value">{confidence_pct:.1f}%</div><div class="progress-bar-container"><div class="progress-bar" style="width:{progress_width}%; background-color:{confidence_color};"></div></div></div>""", unsafe_allow_html=True)
            with cols[1]:
                st.markdown(f"""<div class="custom-card"><div class="card-header">⭐ التوصية</div><div class="card-value">{rec_emoji} {result.get('recommendation', 'N/A')}</div><div style="font-size: 14px; color: #999;">({result.get('strength', 'N/A')})</div></div>""", unsafe_allow_html=True)
            with cols[2]:
                st.markdown(f"""<div class="custom-card"><div class="card-header">📈 سعر الدخول</div><div class="card-value">{format_price(result.get('entry'))}</div></div>""", unsafe_allow_html=True)
            st.markdown("---")
            reason_text = result.get('reason', 'N/A')
            reason_class = "neutral"
            if "صعودية" in reason_text: reason_class = "bullish"
            elif "هبوطية" in reason_text: reason_class = "bearish"
            st.markdown(f"""<div class="trade-plan-card"><div class="trade-plan-title">📝 خطة التداول</div><div class="reason-card {reason_class}"><div class="trade-plan-metric-label">السبب:</div><div class="reason-text">{reason_text}</div></div></div>""", unsafe_allow_html=True)
            profit_pct, loss_pct = calculate_pnl_percentages(result.get('entry'), result.get('take_profit'), result.get('stop_loss'))
            profit_display = f"({profit_pct:.2f}%)" if profit_pct is not None else ""
            loss_display = f"({loss_pct:.2f}%)" if loss_pct is not None else ""
            pnl_cols = st.columns([2, 1])
            with pnl_cols[0]:
                est_time_display = result.get("est_time_to_target")
                time_html_element = f"<span style='font-size: 14px; color: #888; margin-left: 15px;'>⏱️ {est_time_display}</span>" if est_time_display else ""
                st.markdown(f"""<div class="trade-plan-metric"><div class="trade-plan-metric-label">🎯 السعر المستهدف:</div><div class="trade-plan-metric-value">{format_price(result.get('take_profit'))} <span style='font-size: 14px; color: green;'>{profit_display}</span>{time_html_element}</div></div><div class="trade-plan-metric"><div class="trade-plan-metric-label">🛑 وقف الخسارة:</div><div class="trade-plan-metric-value">{format_price(result.get('stop_loss'))} <span style='font-size: 14px; color: red;'>{loss_display}</span></div></div>""", unsafe_allow_html=True)
            with pnl_cols[1]:
                st.markdown(f"""<div class="trade-plan-metric"><div class="trade-plan-metric-label">📈 سعر الدخول:</div><div class="trade-plan-metric-value">{format_price(result.get('entry'))}</div></div>""", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown("### 📊 المقاييس الأساسية")
            metrics_data = result.get("metrics", {})
            weights_data = result.get("weights", {})
            icons = {"funding":"💰", "oi":"📊", "cvd":"📈", "orderbook":"⚖️", "backtest":"🧪", "ema_cross": "📈"}
            available_metrics = {k:v for k,v in metrics_data.items() if v is not None}
            if available_metrics:
                cols = st.columns(len(available_metrics))
                for idx, (k, score) in enumerate(available_metrics.items()):
                    with cols[idx]:
                        weight = weights_data.get(k)
                        weight_display = f"w={weight:.2f}" if weight is not None else ""
                        label_map = {"funding": "التمويل", "oi": "OI", "cvd": "CVD", "orderbook": "الطلبات", "backtest": "الاختبار الخلفي", "ema_cross": "EMA"}
                        st.metric(label=f"{icons.get(k, '⚙️')} {label_map.get(k, k.title())}", value=f"{score:.3f}", delta=weight_display)
            else:
                st.info("لا توجد بيانات مقاييس لعرضها.")
            st.markdown("---")
            st.markdown("### 🔍 تحليل إضافي")
            raw_data = result.get('raw', {})
            st.markdown(f"• **الدعم:** {format_price(raw_data.get('support'))} | **المقاومة:** {format_price(raw_data.get('resistance'))}")
            st.markdown(f"• **حالة السوق:** {raw_data.get('market_regime', 'N/A')} (ADX: {raw_data.get('adx', 'N/A')})")
            if st.checkbox("عرض البيانات الخام للشفافية"):
                st.json(result)

    elif selected_page == "🧮 الحاسبة":
        trading_calculator_app()
    elif selected_page == "📈 المتتبع":
        live_market_tracker()

if __name__ == "__main__":
    render_main_app()

