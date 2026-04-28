import streamlit as st
import random

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== STYLE =====
st.markdown("""
<style>
body {background-color: #0e1117;}
h1, h2, h3, p {color: white;}
.stButton>button {
    background-color: #00adb5;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 200px;
}
</style>
""", unsafe_allow_html=True)

# ===== SESSION =====
if "start" not in st.session_state:
    st.session_state.start = False

# =========================
# 🟢 INTRO PAGE
# =========================
if not st.session_state.start:

    st.title("🌊 Smart Nile Monitoring System")

    st.subheader("📌 What is this project?")

    st.write("""
    A smart system designed to monitor the Nile River using sensors and artificial intelligence.
    It helps detect pollution and harmful plants in real-time.
    """)

    # ===== IMAGES SECTION =====
    col1, col2, col3 = st.columns(3)

    col1.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/PH_Scale.svg", caption="pH Sensor")
    col2.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg", caption="Water Hyacinth")
    col3.image("https://upload.wikimedia.org/wikipedia/commons/e/e3/Nile_River_map.jpg", caption="Nile Location")

    st.subheader("⚙️ System Components")

    st.write("""
    - 📊 Sensors: pH, Turbidity, Temperature, TDS, Ammonia  
    - 📷 AI Camera: Detects harmful plants (like Water Hyacinth)  
    - 📍 GPS: Tracks location in the Nile  
    """)

    st.subheader("🎯 Project Goal")
    st.write("Reduce pollution and protect the Nile using smart monitoring.")

    st.markdown("---")

    if st.button("🚀 Start Live System"):
        st.session_state.start = True
        st.rerun()

# =========================
# 🔵 DASHBOARD
# =========================
else:

    st.title("📊 Live Monitoring Dashboard")

    # ===== SENSORS =====
    st.subheader("📊 Sensors Readings")

    col1, col2, col3 = st.columns(3)

    col1.metric("🌡 Temperature", f"{random.randint(25,32)} °C")
    col2.metric("💧 Turbidity", f"{random.randint(2,8)} NTU")
    col3.metric("⚡ TDS", f"{random.randint(200,400)} ppm")

    col1, col2, col3 = st.columns(3)
    col1.metric("🧪 pH", "7.2")
    col2.metric("☣ Ammonia", "1 mg/L")
    col3.metric("📍 Location", "Cairo, Nile")

    # ===== MAP =====
    st.subheader("🗺 Location Map")
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e3/Nile_River_map.jpg")

    # ===== AI DETECTION =====
    st.subheader("📷 AI Detection")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")
    st.success("Detected: Water Hyacinth (ورد النيل)")
    st.warning("⚠️ This plant indicates pollution")

    # ===== CHATBOT =====
    st.subheader("🤖 Smart Assistant")

    user = st.text_input("Ask about water quality...")

    if user:
        if "ph" in user.lower():
            st.write("pH level is normal ✅")
        elif "pollution" in user.lower():
            st.write("Pollution is moderate ⚠️")
        elif "plant" in user.lower():
            st.write("Detected plant is Water Hyacinth 🌿")
        else:
            st.write("System is working normally 👍")

    if st.button("🔄 Refresh Data"):
        st.rerun()
