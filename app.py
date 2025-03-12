import streamlit as st
import numpy as np
import pickle

# Load trained AI model
with open("dielectric_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Silica Fiber Epoxy Composite - Dielectric Constant Predictor")

# User inputs
fiber_fraction = st.slider("Fiber Fraction (%)", 40, 60, 50)
hardener_type = st.radio("Hardener Type", ("TETA (0)", "DETDA (1)"))
hardener_type = 0 if hardener_type == "TETA (0)" else 1
curing_temp = st.slider("Curing Temperature (°C)", 100, 180, 140)
curing_time = st.slider("Curing Time (hours)", 2, 6, 4)

# Prediction
input_data = np.array([[fiber_fraction, hardener_type, curing_temp, curing_time]])
predicted_k = model.predict(input_data)[0]

# Output result
st.write(f"### Predicted Dielectric Constant (k): {predicted_k:.2f}")

# Footer
st.markdown("---")
st.markdown("**Developed for AI-driven material optimization**")
