import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== DARK STYLE (شيك جدًا) =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #0a0f1c, #111827);
    color: white;
}
h1 {
    text-align: center;
    color: #00c3ff;
    font-size: 50px;
}
h2 {
    color: #4cc9f0;
    margin-top: 40px;
}
p, li {
    font-size: 20px;
    color: #e5e7eb;
}
hr {
    border: 1px solid #333;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🌊 TITLE
# =========================
st.markdown("<h1>🌊 Smart Nile Monitoring System</h1>", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1508780709619-79562169bc64")

st.write("""
The Nile River is one of the most important water resources in the world, especially for Egypt. 
However, it is currently facing serious environmental challenges that threaten water quality and aquatic life.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# ⚠️ PROBLEM (شرح قوي)
# =========================
st.markdown("<h2>⚠️ The Problem</h2>", unsafe_allow_html=True)

st.write("""
One of the major problems in the Nile River is the uncontrolled spread of aquatic plants such as **Water Hyacinth (ورد النيل)**.

These plants:
- Grow very quickly in polluted water  
- Block sunlight from reaching underwater organisms  
- Reduce oxygen levels in water  
- Cause fish death and damage biodiversity  
- Block water flow and affect navigation  
""")

st.image("https://images.unsplash.com/photo-1598514982842-7a6c2c3b6e43")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 💡 SOLUTION
# =========================
st.markdown("<h2>💡 Our Solution</h2>", unsafe_allow_html=True)

st.write("""
To solve this problem, we designed a **Smart Monitoring System** that can analyze water conditions in real-time.

The system works by:
- Collecting data from multiple sensors  
- Using AI to detect harmful plants  
- Sending data to a live monitoring dashboard  
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# ⚙️ COMPONENTS (مفصل)
# =========================
st.markdown("<h2>⚙️ System Components</h2>", unsafe_allow_html=True)

st.write("""
🔹 **Sensors:**
- Temperature → measures water temperature  
- Turbidity → detects water clarity (pollution level)  
- TDS → measures dissolved solids  
- pH → measures acidity/alkalinity  
- Ammonia → detects toxic substances  

🔹 **AI Camera:**
- Captures images of water surface  
- Detects plants like Water Hyacinth  

🔹 **GPS Module:**
- Tracks system location in the Nile  
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 🎯 OBJECTIVE
# =========================
st.markdown("<h2>🎯 Project Objective</h2>", unsafe_allow_html=True)

st.write("""
The main goal of this project is to:
- Monitor water quality continuously  
- Detect pollution early  
- Identify harmful plants automatically  
- Help protect the Nile ecosystem  
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

# AI
st.subheader("📷 AI Detection")

st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6")
st.success("Detected: Water Hyacinth (ورد النيل)")
st.warning("⚠️ Indicates possible pollution")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 💡 CONCLUSION
# =========================
st.markdown("<h2>💡 Conclusion</h2>", unsafe_allow_html=True)

st.write("""
This project provides a smart and efficient solution for monitoring the Nile River.

By combining sensors, AI, and GPS, the system can detect pollution early and support environmental protection efforts.
""")
