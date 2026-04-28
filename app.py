import streamlit as st
import random

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== BACKGROUND + STYLE =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}
h1, h2, h3 {
    color: #00e0ff;
}
p {
    color: #ffffff;
    font-size: 18px;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🌊 TITLE
# =========================
st.markdown("<h1 style='text-align: center;'>🌊 Smart Nile Monitoring System</h1>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# 📌 INTRO
# =========================
st.markdown("<h2>📌 Project Overview</h2>", unsafe_allow_html=True)

st.write("""
This project is a smart system that monitors the Nile River using sensors and AI technology.
It helps detect pollution, monitor water quality, and identify harmful plants.
""")

# =========================
# 🌿 IMAGES (FIXED LINKS)
# =========================
st.markdown("<h2>🌿 Nile Environment</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

col1.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg",
           caption="Water Hyacinth (ورد النيل)")

col2.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Nile_River.jpg",
           caption="Nile River")

# =========================
# ⚙️ COMPONENTS
# =========================
st.markdown("<h2>⚙️ System Components</h2>", unsafe_allow_html=True)

st.write("""
📊 Sensors:
- Temperature  
- Turbidity  
- TDS  
- pH  
- Ammonia  

📷 AI Camera:
- Detects harmful plants  

📍 GPS:
- Tracks location  
""")

# =========================
# 🎯 GOAL
# =========================
st.markdown("<h2>🎯 Project Goal</h2>", unsafe_allow_html=True)

st.write("""
Protect the Nile River by detecting pollution early and monitoring water quality in real-time.
""")

st.markdown("---")

# =========================
# 📊 DASHBOARD
# =========================
st.markdown("<h2>📊 Live Dashboard</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.metric("🌡 Temperature", f"{random.randint(25,32)} °C")
col2.metric("💧 Turbidity", f"{random.randint(2,8)} NTU")
col3.metric("⚡ TDS", f"{random.randint(200,400)} ppm")

col1, col2, col3 = st.columns(3)
col1.metric("🧪 pH", "7.2")
col2.metric("☣ Ammonia", "1 mg/L")
col3.metric("📍 Location", "Cairo, Nile")

# =========================
# 📷 AI DETECTION
# =========================
st.markdown("<h2>📷 AI Detection</h2>", unsafe_allow_html=True)

st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")

st.success("Detected: Water Hyacinth (ورد النيل)")
st.warning("⚠️ This indicates pollution")

# =========================
# 🤖 CHATBOT
# =========================
st.markdown("<h2>🤖 Smart Assistant</h2>", unsafe_allow_html=True)

user = st.text_input("Ask about water quality...")

if user:
    st.write("System is working normally ✅")

# =========================
# 💡 RECOMMENDATIONS
# =========================
st.markdown("<h2>💡 Recommendations</h2>", unsafe_allow_html=True)

st.write("""
- Reduce industrial waste  
- Monitor plants regularly  
- Improve water treatment  
- Increase awareness  
""")
