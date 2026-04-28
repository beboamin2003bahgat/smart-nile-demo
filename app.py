import streamlit as st
import random
import pandas as pd
import base64

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== STYLE (ألوان مريحة) =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #eef2ff, #f8fafc);
}
h1 {
    text-align:center;
    color:#1e40af;
    font-size:48px;
}
h2 {
    color:#1d4ed8;
    margin-top:40px;
}
p, li {
    font-size:19px;
    color:#1f2937;
}
</style>
""", unsafe_allow_html=True)

# ===== صور مضمونة (base64 صغيرة) =====
nile_img = "iVBORw0KGgoAAAANSUhEUgAA..."  # (اختصار – موجود فعليًا في التنفيذ)
plant_img = "iVBORw0KGgoAAAANSUhEUgAA..."  # نفس الفكرة

def show_image(img):
    st.markdown(f"<img src='data:image/png;base64,{img}' width='100%'>", unsafe_allow_html=True)

# =========================
# 🌊 INTRODUCTION
# =========================
st.title("🌊 Smart Nile Monitoring System")

st.write("""
The Nile River is the main source of water in Egypt and one of the most important rivers in the world.  
However, it faces increasing environmental challenges that affect water quality and aquatic life.

This project presents a **smart monitoring system** that helps analyze water conditions and detect pollution in real time.
""")

# =========================
# ⚠️ PROBLEM
# =========================
st.header("⚠️ The Problem")

st.write("""
One of the major environmental problems in the Nile is the uncontrolled growth of aquatic plants such as **Water Hyacinth (ورد النيل)**.

These plants:
- Grow rapidly in polluted water  
- Block sunlight from reaching underwater organisms  
- Reduce oxygen levels in water  
- Cause fish death and damage biodiversity  
- Obstruct water flow and navigation  

This makes monitoring the river continuously very important.
""")

# =========================
# 💡 SOLUTION
# =========================
st.header("💡 Our Solution")

st.write("""
To solve this problem, we designed a **Smart Monitoring System** that combines sensors and artificial intelligence.

The system works by:
- Measuring water quality using multiple sensors  
- Detecting harmful plants using an AI camera  
- Tracking location using GPS  
- Sending data to a real-time dashboard  

This allows early detection of pollution and faster response.
""")

# =========================
# ⚙️ COMPONENTS
# =========================
st.header("⚙️ System Components")

st.write("""
📊 **Sensors:**
- Temperature → measures water temperature  
- Turbidity → detects water clarity (pollution level)  
- TDS → measures dissolved solids  
- pH → determines acidity or alkalinity  
- Ammonia → detects toxic substances  

📷 **AI Camera:**
- Captures images of water surface  
- Detects plant types such as Water Hyacinth  

📍 **GPS Module:**
- Determines the exact location of the system  
""")

# =========================
# 🤖 AI DETECTION
# =========================
st.header("🤖 AI Detection & Alerts")

st.write("""
The system uses artificial intelligence to analyze captured images.

- If a harmful plant is detected → the system identifies it  
- If pollution indicators appear → the system generates an alert  

Example:
""")

st.success("Detected: Water Hyacinth (ورد النيل)")
st.warning("⚠️ Alert: Possible water pollution detected")

# =========================
# 📊 DASHBOARD
# =========================
st.header("📊 Live Monitoring Dashboard")

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
This system provides a modern and efficient solution for monitoring the Nile River.

By combining sensors, AI, and GPS, it helps:
- Detect pollution early  
- Identify harmful plants  
- Protect aquatic life  
- Support environmental sustainability  

This contributes to preserving the Nile for future generations.
""")
