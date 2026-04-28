import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== STYLE (Soft Professional Colors) =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #e3f2fd, #f8fbff);
}
.block-container {
    padding-top: 2rem;
}
h1 {
    text-align:center;
    color:#1565c0;
    font-size:48px;
}
h2 {
    color:#0d47a1;
    margin-top:40px;
}
p, li {
    color:#333;
    font-size:19px;
}
hr {
    border:1px solid #ccc;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🌊 TITLE
# =========================
st.markdown("<h1>🌊 Smart Nile Monitoring System</h1>", unsafe_allow_html=True)

st.write("""
The Nile River is the main source of water in Egypt.  
However, it is facing serious environmental challenges that affect water quality and aquatic life.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Nile_River.jpg")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# ⚠️ PROBLEM
# =========================
st.markdown("<h2>⚠️ The Problem</h2>", unsafe_allow_html=True)

st.write("""
One of the most dangerous problems is the spread of **Water Hyacinth (ورد النيل)**.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")

st.write("""
This plant:
- Grows very fast  
- Blocks sunlight  
- Reduces oxygen in water  
- Causes fish death  
- Affects navigation  
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 💡 SOLUTION
# =========================
st.markdown("<h2>💡 Our Solution</h2>", unsafe_allow_html=True)

st.write("""
We developed a smart system to monitor the Nile using:
- Sensors to measure water quality  
- AI camera to detect plants  
- GPS to track location  
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
Detects Water Hyacinth  
""")

col3.write("""
📍 GPS:
Tracks location  
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 🔄 HOW IT WORKS
# =========================
st.markdown("<h2>🔄 How It Works</h2>", unsafe_allow_html=True)

st.write("""
1. Sensors collect data  
2. Camera captures images  
3. AI detects plants  
4. Data is sent to the dashboard  
""")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 📊 DASHBOARD
# =========================
st.markdown("<h2>📊 Live Monitoring</h2>", unsafe_allow_html=True)

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

st.subheader("📷 AI Detection")

st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")
st.success("Detected: Water Hyacinth")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# 💡 CONCLUSION
# =========================
st.markdown("<h2>💡 Conclusion</h2>", unsafe_allow_html=True)

st.write("""
This system helps monitor water quality, detect pollution, and protect the Nile environment.
""")
