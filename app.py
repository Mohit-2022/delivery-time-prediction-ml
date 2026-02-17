import streamlit as st
import joblib
import pandas as pd

model = joblib.load("delivery_time_model.pkl")

st.title("🚚 Delivery Time Prediction App")

type_of_order = st.selectbox(
    "Type of Order",
    ["Snack", "Drinks", "Meal"]
)

type_of_vehicle = st.selectbox(
    "Vehicle Type",
    ["scooter", "motorcycle", "electric_scooter"]
)

traffic_level = st.selectbox(
    "Traffic Level",
    ["Low", "Moderate", "High"]
)

weather = st.selectbox(
    "Weather",
    ["Clear Sky", "Fog", "overcast clouds"]
)

age = st.slider("Delivery Person Age", 18, 60, 25)
ratings = st.slider("Delivery Person Rating", 1.0, 5.0, 4.5)
temperature = st.slider("Temperature (°C)", 0, 45, 25)
humidity = st.slider("Humidity (%)", 10, 100, 70)
distance = st.slider("Distance (km)", 1, 60, 10)

input_data = pd.DataFrame({
    'Type_of_order': [type_of_order],
    'Type_of_vehicle': [type_of_vehicle],
    'Traffic_Level': [traffic_level],
    'weather_description': [weather],
    'Delivery_person_Age': [age],
    'Delivery_person_Ratings': [ratings],
    'Temperature (0c) ': [temperature],
    'Humidity': [humidity],
    'Distance (km)': [distance]
})

if st.button("Predict Delivery Time"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Delivery Time: {prediction[0]:.2f} minutes")
