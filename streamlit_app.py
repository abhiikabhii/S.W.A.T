import streamlit as st
import random
import time

st.set_page_config(page_title="SWAT-AI Genesis", layout="wide")
st.title("SWAT-AI Genesis — Demo Dashboard")
st.write("Real-time simulated stagnant water monitoring with AI-based risk scoring.")

# Simulated readings
ph = round(random.uniform(6.0, 9.5), 2)
turbidity = round(random.uniform(1.0, 9.0), 2)
flow = round(random.uniform(0.0, 2.0), 2)

st.subheader("🔍 Live Sensor Data (Simulated)")
st.metric("pH Level", ph)
st.metric("Turbidity", turbidity)
st.metric("Flow Rate", f"{flow} L/min")

# Risk Scoring
risk = 0
if ph < 6.5 or ph > 8.5: risk += 30
if turbidity > 5: risk += 40
if flow < 0.2: risk += 50

risk = min(risk, 100)

st.subheader("🧠 AI Risk Score")
st.progress(risk / 100)
st.write(f"### Risk Level: **{risk}/100**")

if risk > 70:
    st.error("High risk of mosquito breeding! Automated treatment recommended.")
elif risk > 40:
    st.warning("Medium risk detected — monitoring closely.")
else:
    st.success("Low risk — water conditions stable.")
