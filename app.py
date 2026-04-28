import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")
st.markdown("""
<style>
/* اخفاء الهيدر بالكامل */
header {visibility: hidden;}

/* اخفاء الفوتر بالكامل */
footer {visibility: hidden;}

/* اخفاء كلمة Hosted with Streamlit */
div[data-testid="stDecoration"] {display: none;}
</style>
""", unsafe_allow_html=True)
# ===== STYLE =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
  background: linear-gradient(135deg,#dbeafe,#f0f9ff);
}
h1{
  text-align:center;
  color:#1e3a8a;
  font-size:50px;
}
h2{
  color:#1d4ed8;
  margin-top:40px;
}
p, li{
  font-size:19px;
  color:#1f2937;
  line-height:1.7;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🌊 INTRODUCTION
# =========================
st.title("🌊 Smart Nile Monitoring System")

st.write("""
The Nile River is the most important water resource in Egypt.  
However, it is facing serious environmental challenges such as pollution and harmful plant growth.

This project introduces a smart system that monitors water quality and detects pollution in real-time using sensors and artificial intelligence.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Nile_River.jpg/800px-Nile_River.jpg")

# =========================
# ⚠️ PROBLEM
# =========================
st.header("⚠️ The Problem")

st.write("""
One of the major problems is the spread of **Water Hyacinth (ورد النيل)**.

This plant:
- Grows very fast  
- Blocks sunlight  
- Reduces oxygen in water  
- Causes fish death  
- Affects water flow  
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Water_hyacinth.jpg/800px-Water_hyacinth.jpg")

# =========================
# 💡 SOLUTION
# =========================
st.header("💡 Our Solution")

st.write("""
We designed a smart monitoring system that:
- Uses sensors to measure water quality  
- Uses AI camera to detect plant types  
- Uses GPS to track location  
- Sends alerts when pollution is detected  
""")

# =========================
# ⚙️ HARDWARE
# =========================
st.header("⚙️ Hardware System")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Arduino_with_sensors.jpg/800px-Arduino_with_sensors.jpg")

st.write("""
The system uses multiple sensors:
- Temperature sensor  
- Turbidity sensor  
- TDS sensor  
- pH sensor  
- Ammonia sensor  

These sensors collect real-time data from water.
""")

# =========================
# 🍓 RASPBERRY PI
# =========================
st.subheader("🍓 Raspberry Pi (Main Controller)")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Raspberry_Pi_4_Model_B_-_Side.jpg/800px-Raspberry_Pi_4_Model_B_-_Side.jpg")

st.write("""
The Raspberry Pi acts as the brain of the system.

It:
- Collects sensor data  
- Processes information  
- Runs AI detection  
- Sends data to the dashboard  
""")

# =========================
# 📷 CAMERA + AI
# =========================
st.header("📷 Camera & AI Detection")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Water_hyacinth.jpg/800px-Water_hyacinth.jpg")

st.success("Detected: Water Hyacinth (ورد النيل)")
st.warning("⚠️ Alert: Possible Pollution Detected")

# =========================
# 📊 DASHBOARD
# =========================
st.header("📊 Live Monitoring Dashboard")

df = pd.DataFrame({'lat':[30.0444],'lon':[31.2357]})
st.map(df)

col1,col2,col3 = st.columns(3)
col1.metric("🌡 Temperature", f"{random.randint(25,32)} °C")
col2.metric("💧 Turbidity", f"{random.randint(2,8)} NTU")
col3.metric("⚡ TDS", f"{random.randint(200,400)} ppm")

col1,col2,col3 = st.columns(3)
col1.metric("🧪 pH", "7.2")
col2.metric("☣ Ammonia", "1 mg/L")
col3.metric("📍 Location", "Cairo")

# =========================
# 🤖 CHATBOT (BUTTON)
# =========================
if "chat" not in st.session_state:
    st.session_state.chat = False

if st.button("💬 Open Chatbot"):
    st.session_state.chat = not st.session_state.chat

if st.session_state.chat:
    st.write("🤖 Ask about the system:")
    msg = st.text_input("Type here...")
    if msg:
        st.write("System is working normally ✅")

# =========================
# 💡 CONCLUSION
# =========================
st.header("💡 Conclusion")

st.write("""
This system helps monitor water quality, detect pollution early, and protect the Nile using smart technology.
""")
st.markdown("""
<style>
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
