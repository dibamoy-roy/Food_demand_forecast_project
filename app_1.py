# app_1.py
import streamlit as st
import pandas as pd
import pickle

# Load Model
MODEL_FILE = "food_demand_forecast.pkl"

@st.cache_resource
def load_model():
    with open(MODEL_FILE, "rb") as f:
        return pickle.load(f)

model = load_model()

st.title("🍽 Food Demand Forecasting")
st.write("Enter the feature values to predict food demand.")

# All feature names used in actual model in correct order
feature_names = [
    "id", "week", "center_id", "meal_id",
    "checkout_price", "base_price",
    "emailer_for_promotion", "homepage_featured"
]

# Collect input values
input_data = {}
for col in feature_names:
    input_data[col] = st.number_input(f"Enter {col}:", value=0.0)

# Predict button
if st.button("Predict"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Demand: {prediction:.2f} orders")