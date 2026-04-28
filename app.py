import streamlit as st
import random

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== STYLE =====
st.markdown("""
<style>
body {background-color: #0e1117;}
h1, h2, h3, p {color: white;}
.block-container {padding-top: 2rem;}
</style>
""", unsafe_allow_html=True)

# =========================
# 🌊 TITLE
# =========================
st.title("🌊 Smart Nile Monitoring System")

st.markdown("---")

# =========================
# 📌 INTRO (PRESENTATION)
# =========================
st.header("📌 Project Overview")

st.write("""
This project is a smart system designed to monitor the Nile River using sensors and artificial intelligence.

It helps in:
- Detecting water pollution
- Monitoring water quality
- Identifying harmful plants like Water Hyacinth
""")

# =========================
# 🌿 IMAGES
# =========================
st.header("🌿 Nile Environment")

col1, col2 = st.columns(2)

col1.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg", caption="Water Hyacinth (ورد النيل)")
col2.image("https://upload.wikimedia.org/wikipedia/commons/e/e3/Nile_River_map.jpg", caption="Nile River")

# =========================
# ⚙️ COMPONENTS
# =========================
st.header("⚙️ System Components")

st.write("""
🔹 Sensors:
- Temperature  
- Turbidity  
- TDS  
- pH  
- Ammonia  

🔹 AI Camera:
- Detects harmful plants  

🔹 GPS:
- Tracks location in the Nile  
""")

# =========================
# 🎯 GOAL
# =========================
st.header("🎯 Project Goal")

st.write("""
To protect the Nile River by detecting pollution early and monitoring water quality in real-time.
""")

st.markdown("---")

# =========================
# 📊 DASHBOARD (AT THE END)
# =========================
st.header("📊 Live System Dashboard")

# Sensors
col1, col2, col3 = st.columns(3)

col1.metric("🌡 Temperature", f"{random.randint(25,32)} °C")
col2.metric("💧 Turbidity", f"{random.randint(2,8)} NTU")
col3.metric("⚡ TDS", f"{random.randint(200,400)} ppm")

col1, col2, col3 = st.columns(3)
col1.metric("🧪 pH", "7.2")
col2.metric("☣ Ammonia", "1 mg/L")
col3.metric("📍 Location", "Cairo, Nile")

# =========================
# 📷 AI DETECTION
# =========================
st.subheader("📷 AI Plant Detection")

st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")
st.success("Detected: Water Hyacinth (ورد النيل)")
st.warning("⚠️ This indicates possible pollution")

# =========================
# 🤖 CHATBOT
# =========================
st.subheader("🤖 Smart Assistant")

user = st.text_input("Ask about water quality...")

if user:
    if "ph" in user.lower():
        st.write("pH is normal ✅")
    elif "pollution" in user.lower():
        st.write("Pollution level is moderate ⚠️")
    else:
        st.write("System is working normally 👍")

# =========================
# 💡 RECOMMENDATIONS
# =========================
st.subheader("💡 Recommendations")

st.write("""
- Reduce industrial waste dumping  
- Monitor harmful plants regularly  
- Improve water treatment systems  
- Increase environmental awareness  
""")
