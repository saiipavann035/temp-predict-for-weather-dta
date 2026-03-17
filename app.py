# app.py

import streamlit as st
from main import load_model, predict_temperature

# Title
st.title("🌡️ Temperature Prediction using ML")
st.write("Predict future temperature based on historical weather data")

# Load model
model = load_model()

# Date input
date_input = st.date_input("Select a date to predict temperature")

# Predict button
if st.button("Predict Temperature"):
    result = predict_temperature(model, date_input)
    st.success(f"Predicted Temperature: {result:.2f} °C")

# Footer
st.markdown("---")
st.write("Built with Streamlit & Machine Learning")