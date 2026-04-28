import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== STYLE =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
}
h1, h2, h3 {
    color: #00e0ff;
}
p, li {
    color: white;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ===== TITLE =====
st.markdown("<h1 style='text-align:center;'>🌊 Smart Nile Monitoring System</h1>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# 📌 INTRO
# =========================
st.header("📌 Project Overview")

st.write("""
The Nile River faces serious environmental problems such as pollution and the spread of harmful plants like Water Hyacinth.

This project introduces a smart system that monitors water quality using sensors, GPS, and AI.
""")

# =========================
# 🌿 IMAGES
# =========================
col1, col2 = st.columns(2)

col1.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg",
           caption="Water Hyacinth (ورد النيل)")

col2.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Nile_River.jpg",
           caption="Nile River")

# =========================
# ⚙️ COMPONENTS
# =========================
st.header("⚙️ System Components")

st.write("""
🔹 Sensors:
- Temperature
- Turbidity
- TDS
- pH
- Ammonia

🔹 AI Camera:
Detects harmful plants such as Water Hyacinth

🔹 GPS:
Tracks location in the Nile
""")

# =========================
# 🎯 OBJECTIVE
# =========================
st.header("🎯 Project Objective")

st.write("""
Monitor water quality in real-time and detect pollution early to protect the Nile ecosystem.
""")

st.markdown("---")

# =========================
# 🗺 GPS MAP
# =========================
st.header("🗺 Live Location")

df = pd.DataFrame({
    'lat': [30.0444],
    'lon': [31.2357]
})

st.map(df)

# =========================
# 📊 DASHBOARD
# =========================
st.header("📊 Live Sensors Data")

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
st.header("📷 AI Plant Detection")

st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")
st.success("Detected: Water Hyacinth (ورد النيل)")
st.warning("⚠️ This plant indicates pollution")

# =========================
# 🤖 CHATBOT (FAKE UI)
# =========================
st.sidebar.title("🤖 Chatbot")

msg = st.sidebar.text_input("Ask something...")

if msg:
    st.sidebar.write("System is working normally ✅")

# =========================
# 💡 CONCLUSION
# =========================
st.header("💡 Conclusion")

st.write("""
This system provides a smart solution to monitor the Nile River using sensors and AI.

It helps reduce pollution, detect harmful plants, and protect the environment.
""")
