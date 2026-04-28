import streamlit as st
import random

st.set_page_config(page_title="Smart Nile", layout="wide")

# ===== STYLE =====
st.markdown("""
<style>
body {background-color: #0e1117;}
h1, h2, h3, p {color: white;}
</style>
""", unsafe_allow_html=True)

# ===== SESSION =====
if "start" not in st.session_state:
    st.session_state.start = False

# ================= INTRO =================
if not st.session_state.start:

    st.title("🌊 Smart Nile Monitoring System")

    st.subheader("📌 What is this project?")
    st.write("A smart system to monitor Nile water quality using sensors and AI.")

    col1, col2, col3 = st.columns(3)

    col1.image("https://images.unsplash.com/photo-1581090700227-1e8a1bcb5d9b")
    col2.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb")
    col3.image("https://images.unsplash.com/photo-1470770841072-f978cf4d019e")

    st.subheader("⚙️ System Components")
    st.write("""
    - Sensors: pH, Turbidity, Temperature, TDS, Ammonia  
    - AI Camera: Detects plants  
    - GPS: Tracks location  
    """)

    st.subheader("🎯 Goal")
    st.write("Protect the Nile and detect pollution early.")

    if st.button("🚀 Start System"):
        st.session_state.start = True
        st.rerun()

# ================= DASHBOARD =================
else:

    st.title("📊 Live Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Temperature", f"{random.randint(25,32)} °C")
    col2.metric("Turbidity", f"{random.randint(2,8)} NTU")
    col3.metric("TDS", f"{random.randint(200,400)} ppm")

    st.subheader("📷 AI Detection")
    st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6")
    st.success("Detected: Water Plant")

    st.subheader("🤖 Chatbot")
    user = st.text_input("Ask anything...")
    if user:
        st.write("System is working fine ✅")
