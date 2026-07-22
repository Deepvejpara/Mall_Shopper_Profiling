import streamlit as st
import joblib
import numpy as np

# Load model & scaler
model = joblib.load("mall_segmentation_model.pkl")
scaler = joblib.load("mall_scaler.pkl")

st.title("🛍️ Customer Persona Predictor")

st.write("Enter customer details:")

# Inputs (adjust based on your model features)
age = st.number_input("Age", min_value=10, max_value=100, value=25)
annual_income = st.number_input("Annual Income (k$)", min_value=0, max_value=200, value=50)
spending_score = st.number_input("Spending Score (1-100)", min_value=1, max_value=100, value=50)

# Predict button
if st.button("Predict Persona"):
    
    # Prepare input
    input_data = np.array([[annual_income, spending_score]])
    
    # Scale input
    scaled_data = scaler.transform(input_data)
    
    # Predict cluster/persona
    prediction = model.predict(scaled_data)
    
    st.success(f"Predicted Customer Persona: {prediction[0]}")