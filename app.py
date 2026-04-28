import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== STYLE (واضح + مريح) =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #f0f6ff;
}
h1 {
    text-align:center;
    color:#0b3c5d;
}
h2 {
    color:#145da0;
    margin-top:40px;
}
p, li {
    color:#333;
    font-size:20px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🟢 INTRODUCTION
# =========================
st.title("🌊 Smart Nile Monitoring System")

st.write("""
This project is designed to **monitor the Nile River in real-time** using smart technology.

The system helps detect pollution, analyze water quality, and identify harmful plants automatically.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Nile_River.jpg")

# =========================
# ⚠️ PROBLEM
# =========================
st.header("⚠️ The Problem")

st.write("""
The Nile River faces serious environmental challenges such as:

- Water pollution  
- Spread of harmful plants like **Water Hyacinth (ورد النيل)**  
- Decreasing water quality  

These problems affect aquatic life and water safety.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")

# =========================
# 💡 SOLUTION
# =========================
st.header("💡 Our Solution")

st.write("""
We developed a **Smart Monitoring System** that:

- Measures water quality using sensors  
- Detects plant types using AI camera  
- Tracks location using GPS  
- Sends real-time data to a dashboard  
""")

# =========================
# ⚙️ COMPONENTS (مفهومة)
# =========================
st.header("⚙️ System Components")

st.write("""
📊 **Sensors:**
- Temperature → measures water temperature  
- Turbidity → detects pollution level  
- TDS → measures dissolved solids  
- pH → checks water balance  
- Ammonia → detects toxic substances  

📷 **AI Camera:**
- Detects plant type  
- Identifies Water Hyacinth  

📍 **GPS:**
- Shows location on map  
""")

# =========================
# 🤖 AI DETECTION
# =========================
st.header("🤖 AI Detection & Alerts")

st.write("""
The system uses AI to analyze images from the camera.

- If a harmful plant is detected → system identifies it  
- If pollution is detected → system sends an alert  

Example:
""")

st.success("Detected: Water Hyacinth (ورد النيل)")
st.warning("⚠️ Alert: Possible water pollution detected")

# =========================
# 📊 DASHBOARD
# =========================
st.header("📊 Live Monitoring Dashboard")

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

col1, col2, col3 = st.columns(3)

col1.metric("🧪 pH", "7.2")
col2.metric("☣ Ammonia", "1 mg/L")
col3.metric("📍 Location", "Cairo")

# =========================
# 💡 CONCLUSION
# =========================
st.header("💡 Conclusion")

st.write("""
This system provides a smart way to monitor the Nile River.

It helps detect pollution early, identify harmful plants, and protect the environment using modern technology.
""")
