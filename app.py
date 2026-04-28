import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== STYLE (ألوان واضحة + زرار دائري) =====
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
  background: linear-gradient(135deg,#e6f2ff,#f8fbff);
}
.block-container{padding-top:2rem;}
h1{ text-align:center; color:#0b3c5d; font-size:52px;}
h2{ color:#145da0; margin-top:40px;}
p, li{ color:#1f2937; font-size:19px; line-height:1.7;}
.chat-btn{
  position:fixed; bottom:25px; right:25px;
  background:#2563eb; color:white; border:none;
  border-radius:50%; width:60px; height:60px;
  font-size:28px; cursor:pointer; box-shadow:0 6px 20px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🌊 BIG INTRO (Presentation)
# =========================
st.title("🌊 Smart Nile Monitoring System")

st.write("""
The Nile River is the main source of water in Egypt and one of the most important rivers in the world.  
Millions of people depend on it for drinking water, agriculture, and daily life.

However, the Nile is currently facing serious environmental challenges that threaten its quality and sustainability.
These challenges require continuous monitoring and smart solutions.
""")

st.write("""
This project introduces a **Smart Monitoring System** that uses modern technology to analyze water conditions
and detect environmental problems in real-time.

The system combines:
- Sensors  
- Artificial Intelligence  
- GPS Tracking  

to provide accurate and instant information about the river.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Nile_River.jpg/800px-Nile_River.jpg")

# =========================
# ⚠️ PROBLEM (شرح كبير)
# =========================
st.header("⚠️ The Problem")

st.write("""
One of the most serious environmental problems in the Nile River is the spread of harmful aquatic plants,
especially **Water Hyacinth (ورد النيل)**.

This plant grows very quickly in polluted water and causes multiple issues:
""")

st.write("""
- Blocks sunlight from reaching underwater organisms  
- Reduces oxygen levels in water  
- Causes fish death  
- Affects biodiversity  
- Blocks water flow and navigation  
""")

st.write("""
In addition to plant growth, water pollution from industrial and human activities also affects water quality.
Without continuous monitoring, these problems can become more dangerous over time.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Water_hyacinth.jpg/800px-Water_hyacinth.jpg")

# =========================
# 💡 SOLUTION (شرح واضح)
# =========================
st.header("💡 Our Solution")

st.write("""
To solve these problems, we developed a **Smart Nile Monitoring System**.

The system continuously monitors water conditions and provides real-time data to users.
""")

st.write("""
It works by:
- Collecting data from sensors  
- Capturing images using a camera  
- Analyzing data using AI  
- Sending results to a dashboard  
""")

st.write("""
If the system detects pollution or harmful plants, it generates alerts immediately.
""")

# =========================
# ⚙️ COMPONENTS (مفصل)
# =========================
st.header("⚙️ System Components")

st.write("""
📊 **Sensors:**
- Temperature → measures water temperature  
- Turbidity → detects water clarity  
- TDS → measures dissolved solids  
- pH → measures acidity  
- Ammonia → detects toxic substances  

📷 **Camera + AI:**
- Captures water surface  
- Detects plant type  
- Identifies harmful plants  

📍 **GPS Module:**
- Tracks system location  
""")

# =========================
# 🤖 AI DETECTION + ALERT
# =========================
st.header("🤖 AI Detection & Alerts")

st.write("""
The AI model analyzes images captured by the camera.

- If a plant is detected → system identifies its type  
- If pollution indicators appear → system sends alert  
""")

st.success("Detected: Water Hyacinth (ورد النيل)")
st.warning("⚠️ Alert: Possible Pollution Detected")

# =========================
# 📊 DASHBOARD
# =========================
st.header("📊 Live Monitoring Dashboard")

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

# =========================
# 💬 CHATBOT ICON (تحت)
# =========================
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False

# زرار دائري
if st.markdown('<button class="chat-btn">💬</button>', unsafe_allow_html=True):
    st.session_state.chat_open = not st.session_state.chat_open

# نافذة الشات
if st.session_state.chat_open:
    st.markdown("### 🤖 Assistant")
    user = st.text_input("Ask about the project...")
    if user:
        if "sensor" in user.lower():
            st.write("Sensors measure water quality parameters like pH and turbidity.")
        elif "pollution" in user.lower():
            st.write("The system detects pollution using turbidity, ammonia, and AI.")
        else:
            st.write("This system monitors the Nile using AI and sensors.")
