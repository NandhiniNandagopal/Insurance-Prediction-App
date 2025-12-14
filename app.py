import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Insurance Premium Predictor")
st.write("Enter your age to predict your insurance premium.")

# User input
age = st.number_input("Age", min_value=18, max_value=100, value=30)

# Prediction
if st.button("Predict"):
    input_data = np.array([[age]])
    premium = model.predict(input_data)
    st.success(f"Estimated Insurance Premium: ₹{premium[0]:.2f}")

