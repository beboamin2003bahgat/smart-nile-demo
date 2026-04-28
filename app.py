import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== CLEAN DARK STYLE =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #0b132b;
}
.block-container {
    padding-top: 2rem;
}
h1 {
    text-align:center;
    color:#5bc0be;
    font-size:48px;
}
h2 {
    color:#f1faee;
    margin-top:50px;
}
p, li {
    color:#e0fbfc;
    font-size:19px;
}
hr {
    border:1px solid #1c2541;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🌊 INTRO (HOOK)
# =========================
st.markdown("<h1>🌊 Smart Nile Monitoring System</h1>", unsafe_allow_html=True)

st.write("""
The Nile River is the main source of life in Egypt.  
But today, it faces increasing pollution and environmental threats that affect water quality and aquatic life.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Nile_River.jpg")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# ⚠️ PROBLEM
# =========================
st.markdown("<h2>⚠️ The Problem</h2>", unsafe_allow_html=True)

st.write("""
One of the most serious problems is the uncontrolled spread of **Water Hyacinth (ورد النيل)**.

This plant:
- Grows very fast in polluted water  
- Blocks sunlight  
- Reduces oxygen in water  
- Causes fish death  
- Affects navigation and water flow  
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 💥 IMPACT
# =========================
st.markdown("<h2>💥 Impact on Environment</h2>", unsafe_allow_html=True)

st.write("""
These problems lead to:
- Loss of aquatic life  
- Poor water quality  
- Environmental imbalance  
- Increased cost of water treatment  
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 💡 SOLUTION
# =========================
st.markdown("<h2>💡 Our Solution</h2>", unsafe_allow_html=True)

st.write("""
We designed a smart system that monitors the Nile in real-time using sensors, AI, and GPS.

The system can:
- Measure water quality  
- Detect harmful plants  
- Track location  
- Send data to a dashboard  
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# ⚙️ COMPONENTS
# =========================
st.markdown("<h2>⚙️ System Components</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.write("""
📊 **Sensors**
- Temperature  
- Turbidity  
- TDS  
- pH  
- Ammonia  
""")

col2.write("""
📷 **AI Camera**
- Detects Water Hyacinth  
- Identifies pollution indicators  
""")

col3.write("""
📍 **GPS Module**
- Tracks system location  
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 🔄 HOW IT WORKS
# =========================
st.markdown("<h2>🔄 How the System Works</h2>", unsafe_allow_html=True)

st.write("""
1. Sensors collect water data  
2. Camera captures images  
3. AI analyzes the images  
4. Data is sent to the dashboard  
5. User monitors everything in real-time  
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

col1, col2, col3 = st.columns(3)

col1.metric("🧪 pH", "7.2")
col2.metric("☣ Ammonia", "1 mg/L")
col3.metric("📍 Location", "Cairo")

# AI Detection
st.subheader("📷 AI Detection")

st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")
st.success("Detected: Water Hyacinth")
st.warning("⚠️ Pollution Indicator")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 💡 CONCLUSION
# =========================
st.markdown("<h2>💡 Conclusion</h2>", unsafe_allow_html=True)

st.write("""
This system provides a smart and efficient way to monitor the Nile.

It helps detect pollution early, protect the environment, and support sustainable water management.
""")
