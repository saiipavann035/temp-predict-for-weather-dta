# app.py

import streamlit as st
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

.stButton>button {
    background: linear-gradient(45deg, #ff6a00, #ee0979);
    color: white;
    border-radius: 10px;
    padding: 10px 25px;
    font-size: 16px;
    border: none;
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
st.markdown('<div class="subtitle">Predict temperature using Machine Learning</div>', unsafe_allow_html=True)

# Load model
model = load_model()

# Card UI
st.markdown('<div class="card">', unsafe_allow_html=True)

date_input = st.date_input("📅 Select a date")

if st.button("🔮 Predict Temperature"):
    result = predict_temperature(model, date_input)

    # Dynamic color based on temperature
    if result < 10:
        color = "#00c6ff"   # cold (blue)
        emoji = "❄️"
    elif result < 25:
        color = "#00ff95"   # normal (green)
        emoji = "🌤️"
    else:
        color = "#ff5733"   # hot (red/orange)
        emoji = "🔥"

    st.markdown(
        f'<div class="result" style="color:{color};">{emoji} {result:.2f} °C</div>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Machine Learning")