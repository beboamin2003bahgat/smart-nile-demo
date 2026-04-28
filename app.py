import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== UI STYLE (ألوان شيك) =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #dbeafe, #eff6ff);
}
h1 {
    text-align:center;
    color:#1e3a8a;
    font-size:50px;
}
h2 {
    color:#1d4ed8;
    margin-top:40px;
}
p, li {
    font-size:20px;
    color:#1f2937;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🌊 INTRO
# =========================
st.title("🌊 Smart Nile Monitoring System")

st.write("""
This project is designed to monitor the Nile River using sensors and AI.
It helps detect pollution and identify harmful plants in real-time.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Nile_River.jpg/800px-Nile_River.jpg")

# =========================
# ⚠️ PROBLEM
# =========================
st.header("⚠️ The Problem")

st.write("""
The Nile River suffers from pollution and the spread of harmful plants like Water Hyacinth.
These problems affect water quality and aquatic life.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Water_hyacinth.jpg/800px-Water_hyacinth.jpg")

# =========================
# 💡 SOLUTION
# =========================
st.header("💡 Our Solution")

st.write("""
We built a smart system that:
- Measures water quality using sensors  
- Detects plants using AI  
- Tracks location using GPS  
""")

# =========================
# ⚙️ COMPONENTS
# =========================
st.header("⚙️ System Components")

st.write("""
📊 Sensors:
- Temperature  
- Turbidity  
- TDS  
- pH  
- Ammonia  

📷 AI Camera:
- Detects plant type  

📍 GPS:
- Shows location on map  
""")

# =========================
# 🤖 AI DETECTION
# =========================
st.header("🤖 AI Detection")

st.success("Detected: Water Hyacinth")
st.warning("⚠️ Alert: Pollution detected")

# =========================
# 📊 DASHBOARD
# =========================
st.header("📊 Live Dashboard")

df = pd.DataFrame({
    'lat': [30.0444],
    'lon': [31.2357]
})
st.map(df)

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
This system helps detect pollution early and protect the Nile using smart technology.
""")
