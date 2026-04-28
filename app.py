import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== STYLE =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f8f9fa;
}
h1 {
    text-align: center;
    color: #0077b6;
    font-size: 48px;
}
h2 {
    color: #023e8a;
    margin-top: 40px;
}
p {
    font-size: 20px;
    color: #333;
}
hr {
    border: 1px solid #ccc;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🌊 TITLE
# =========================
st.markdown("<h1>🌊 Smart Nile Monitoring System</h1>", unsafe_allow_html=True)

st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Nile_River.jpg")

st.write("""
A smart system designed to monitor the Nile River using sensors, AI, and GPS technology.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# ⚠️ PROBLEM
# =========================
st.markdown("<h2>⚠️ The Problem</h2>", unsafe_allow_html=True)

st.write("""
The Nile River is facing serious environmental problems:
- Water pollution
- Spread of harmful plants
- Decrease in water quality
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg",
         caption="Water Hyacinth (ورد النيل)")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 💡 SOLUTION
# =========================
st.markdown("<h2>💡 Our Solution</h2>", unsafe_allow_html=True)

st.write("""
We developed a smart system that:
- Monitors water quality using sensors
- Detects harmful plants using AI
- Tracks location using GPS
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# ⚙️ COMPONENTS
# =========================
st.markdown("<h2>⚙️ System Components</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.write("""
📊 Sensors:
- Temperature
- Turbidity
- TDS
- pH
- Ammonia
""")

col2.write("""
📷 AI Camera:
Detects plants like Water Hyacinth
""")

col3.write("""
📍 GPS Module:
Tracks location in Nile
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 🎯 OBJECTIVE
# =========================
st.markdown("<h2>🎯 Project Objective</h2>", unsafe_allow_html=True)

st.write("""
To monitor the Nile in real-time and reduce pollution using smart technology.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 📊 DASHBOARD
# =========================
st.markdown("<h2>📊 Live Monitoring Dashboard</h2>", unsafe_allow_html=True)

# MAP
df = pd.DataFrame({
    'lat': [30.0444],
    'lon': [31.2357]
})
st.map(df)

# Sensors
col1, col2, col3 = st.columns(3)

col1.metric("🌡 Temperature", f"{random.randint(25,32)} °C")
col2.metric("💧 Turbidity", f"{random.randint(2,8)} NTU")
col3.metric("⚡ TDS", f"{random.randint(200,400)} ppm")

# AI Detection
st.subheader("📷 AI Detection")

st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")
st.success("Detected: Water Hyacinth")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 💡 CONCLUSION
# =========================
st.markdown("<h2>💡 Conclusion</h2>", unsafe_allow_html=True)

st.write("""
This system provides a smart solution to monitor and protect the Nile River.

It helps detect pollution early and supports environmental sustainability.
""")
