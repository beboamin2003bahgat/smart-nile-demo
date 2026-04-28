import streamlit as st

st.set_page_config(page_title="Smart Nile", layout="wide")

st.title("🌊 Smart Nile Monitoring System")

st.header("📊 Sensors Readings")

col1, col2, col3 = st.columns(3)

col1.metric("🌡 Temperature", "28 °C")
col2.metric("💧 Turbidity", "5 NTU")
col3.metric("⚡ TDS", "320 ppm")

col1, col2, col3 = st.columns(3)
col1.metric("🧪 pH", "7.2")
col2.metric("☣ Ammonia", "1 mg/L")
col3.metric("📍 GPS", "Cairo, Nile")

st.header("🗺 Location")
st.image("https://upload.wikimedia.org/wikipedia/commons/e/e3/Nile_River_map.jpg")

st.header("📷 Plant Detection")
st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Water_hyacinth.jpg")
st.success("Detected: Water Hyacinth (ورد النيل)")