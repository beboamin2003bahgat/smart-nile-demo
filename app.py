import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== LIGHT STYLE =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f5f7fa;
}
h1 {
    color: #0077b6;
    text-align: center;
}
h2 {
    color: #023e8a;
}
p, li {
    font-size: 18px;
    color: #333;
}
</style>
""", unsafe_allow_html=True)

# ===== NAVIGATION =====
page = st.sidebar.radio("📌 Navigate", [
    "🏠 Home",
    "⚠️ Problem",
    "💡 Solution",
    "⚙️ Components",
    "📊 Dashboard"
])

# =========================
# 🏠 HOME
# =========================
if page == "🏠 Home":
    st.title("🌊 Smart Nile Monitoring System")

    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Nile_River.jpg")

    st.write("""
    A smart system designed to monitor the Nile River using sensors, AI, and GPS technology.
    
    Our goal is to detect pollution early and protect the environment.
    """)

# =========================
# ⚠️ PROBLEM
# =========================
elif page == "⚠️ Problem":
    st.header("⚠️ The Problem")

    st.write("""
    The Nile River faces serious challenges such as:
    - Water pollution
    - Spread of harmful plants
    - Decreasing water quality
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg",
             caption="Water Hyacinth (ورد النيل)")

# =========================
# 💡 SOLUTION
# =========================
elif page == "💡 Solution":
    st.header("💡 Our Solution")

    st.write("""
    We developed a smart system that:
    - Monitors water quality using sensors
    - Detects harmful plants using AI
    - Tracks location using GPS
    """)

# =========================
# ⚙️ COMPONENTS
# =========================
elif page == "⚙️ Components":
    st.header("⚙️ System Components")

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

# =========================
# 📊 DASHBOARD
# =========================
elif page == "📊 Dashboard":
    st.header("📊 Live Monitoring")

    df = pd.DataFrame({
        'lat': [30.0444],
        'lon': [31.2357]
    })
    st.map(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Temperature", f"{random.randint(25,32)} °C")
    col2.metric("Turbidity", f"{random.randint(2,8)} NTU")
    col3.metric("TDS", f"{random.randint(200,400)} ppm")

    st.subheader("📷 AI Detection")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")

    st.success("Detected: Water Hyacinth")
