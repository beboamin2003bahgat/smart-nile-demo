import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== STYLE (واضح ومختلف) =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
  background: linear-gradient(135deg,#e0f7ff,#f5fbff);
}
h1{ text-align:center; color:#0b3c5d; font-size:48px;}
h2{ color:#145da0; margin-top:35px;}
p, li{ color:#1f2937; font-size:19px;}
</style>
""", unsafe_allow_html=True)

# ===== INTRO =====
st.title("🌊 Smart Nile Monitoring System")

st.write("""
A smart system to monitor the Nile River using sensors, AI, and GPS.
It detects pollution, analyzes water quality, and identifies harmful plants.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Nile_River.jpg/800px-Nile_River.jpg")

# ===== PROBLEM =====
st.header("⚠️ The Problem")
st.write("""
The Nile suffers from pollution and harmful plants like Water Hyacinth,
which affect water quality and aquatic life.
""")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Water_hyacinth.jpg/800px-Water_hyacinth.jpg")

# ===== SOLUTION =====
st.header("💡 Our Solution")
st.write("""
We built a system that:
- Measures water quality (sensors)
- Detects plants (AI camera)
- Tracks location (GPS)
- Sends alerts for pollution
""")

# ===== CAMERA SECTION =====
st.header("📷 Camera & AI Detection")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Water_hyacinth.jpg/800px-Water_hyacinth.jpg")
st.success("Detected: Water Hyacinth")
st.warning("⚠️ Pollution Alert")

# ===== DASHBOARD =====
st.header("📊 Live Monitoring")

df = pd.DataFrame({'lat':[30.0444],'lon':[31.2357]})
st.map(df)

col1,col2,col3 = st.columns(3)
col1.metric("Temperature", f"{random.randint(25,32)} °C")
col2.metric("Turbidity", f"{random.randint(2,8)} NTU")
col3.metric("TDS", f"{random.randint(200,400)} ppm")

col1,col2,col3 = st.columns(3)
col1.metric("pH", "7.2")
col2.metric("Ammonia", "1 mg/L")
col3.metric("Location", "Cairo")

# ===== CHATBOT SIDEBAR =====
st.sidebar.title("🤖 Chatbot")
msg = st.sidebar.text_input("Ask me...")

if msg:
    if "ph" in msg.lower():
        st.sidebar.write("pH is normal ✅")
    elif "pollution" in msg.lower():
        st.sidebar.write("Pollution detected ⚠️")
    else:
        st.sidebar.write("System working normally 👍")
