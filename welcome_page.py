import streamlit as st

def render_welcome_page():
    
    # --- HTML الخاص بالخلفية والمحتوى ---
    st.markdown("""
        <video autoplay muted loop id="video-background">
            <source src="https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-brain-with-synapses-29584-large.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        
        <div class="overlay"></div>

        <div class="welcome-container">
            <h1 class="glowing-title">SIGNAL PRIME</h1>
            <p class="welcome-subtitle">Where Data Meets Decision.</p>
        </div>
    """, unsafe_allow_html=True)

    # --- زر البدء (يتم وضعه خارج الـ markdown ليعمل بشكل صحيح) ---
    if st.button("🚀 Launch Scanner", key="launch_scanner_final_version"):
        st.session_state.show_welcome_page = False
        st.rerun()
