import streamlit as st
import numpy as np
import pickle
from pathlib import Path
# Page configuration
st.set_page_config(page_title="Calorie Burn Predictor", page_icon="🔥", layout="centered")

st.title("🔥 Calorie Burn Predictor")
st.write("Predict the calories burned during your workout using Machine Learning!")

# Load Pipeline Object (Model + Scaler inside)
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / 'artifacts' / 'model.pkl'

with open(MODEL_PATH, 'rb') as f:
    pipeline = pickle.load(f)

# User Inputs Form
st.header("Enter Workout & User Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age (years)", min_value=10, max_value=100, value=25)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)

with col2:
    duration = st.number_input("Workout Duration (minutes)", min_value=1.0, max_value=300.0, value=30.0)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=60.0, max_value=220.0, value=110.0)
    body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=38.5)



# Predict Button
if st.button("Predict Calories Burned", type="primary"):
    # Raw Input Data (Pipeline will handle scaling automatically!)
    input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
    
    # Direct Prediction through Pipeline
    prediction = pipeline.predict(input_data)
    
    # Display Result
    st.success(f"🔥 **Estimated Calories Burned:** {prediction[0]:.2f} kcal")