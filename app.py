# app.py

import streamlit as st
import pandas as pd
import time
from main import load_model, predict_temperature

# Page config
st.set_page_config(
    page_title="Temperature Predictor",
    page_icon="🌡️",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #ffffff;
}
.subtitle {
    text-align: center;
    color: #cfd8dc;
    margin-bottom: 30px;
}
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}
.result {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌡️ Temperature Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Live prediction using Machine Learning</div>', unsafe_allow_html=True)

# Load model
model = load_model()

# Load dataset (for chart)
df = pd.read_csv("large_temperature_dataset.csv")
df['date'] = pd.to_datetime(df['date'])

# Card
st.markdown('<div class="card">', unsafe_allow_html=True)

# Date input (LIVE trigger)
date_input = st.date_input("📅 Select a date")

# ⏳ Loading animation
with st.spinner("Predicting temperature..."):
    time.sleep(1)  # simulate loading
    result = predict_temperature(model, date_input)

# 🎨 Dynamic color
if result < 10:
    color = "#00c6ff"
    emoji = "❄️"
elif result < 25:
    color = "#00ff95"
    emoji = "🌤️"
else:
    color = "#ff5733"
    emoji = "🔥"

# 🌡️ Result
st.markdown(
    f'<div class="result" style="color:{color};">{emoji} {result:.2f} °C</div>',
    unsafe_allow_html=True
)

# 📊 Chart
st.markdown("### 📊 Temperature Trend")

# Add predicted point to dataset
new_row = pd.DataFrame({
    "date": [pd.to_datetime(date_input)],
    "temp": [result]
})

df_chart = pd.concat([df, new_row])

# Sort by date
df_chart = df_chart.sort_values("date")

# Plot
st.line_chart(df_chart.set_index("date"))

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Machine Learning")