# app.py

import streamlit as st
from main import load_model, predict_temperature

# Page config
st.set_page_config(
    page_title="Temperature Predictor",
    page_icon="🌡️",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #74ebd5, #ACB6E5);
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
    }
    .subtitle {
        text-align: center;
        color: #f0f0f0;
        margin-bottom: 30px;
    }
    .card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    }
    .result {
        font-size: 28px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌡️ Temperature Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict temperature using Machine Learning</div>', unsafe_allow_html=True)

# Load model
model = load_model()

# Card container
st.markdown('<div class="card">', unsafe_allow_html=True)

# Date input
date_input = st.date_input("📅 Select a date")

# Predict button
if st.button("🔮 Predict Temperature"):
    result = predict_temperature(model, date_input)
    st.markdown(f'<div class="result">🌡️ {result:.2f} °C</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Machine Learning")