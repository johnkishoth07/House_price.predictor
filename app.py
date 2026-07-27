import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")
st.write("Enter the house details below")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("house_predictor.pkl")

model = load_model()

# Inputs (NO commas at the end)
Area = st.number_input("Area(sq feet)", min_value=2000, max_value=16200, step=1)
Bedrooms = st.number_input("Bedrooms(1 to 6)", min_value=1, max_value=6, step=1)
bathrooms = st.number_input("Bathrooms(1 to 4)", min_value=1, max_value=4, step=1)
stories = st.number_input("Stories(1,4)", min_value=1, max_value=4, step=1)
mainroad = st.number_input("Main Road (0=No, 1=Yes)", min_value=0, max_value=1, step=1)
guestroom = st.number_input("Guest Room (0=No, 1=Yes)", min_value=0, max_value=1, step=1)
basement = st.number_input("Basement (0=No, 1=Yes)", min_value=0, max_value=1, step=1)
hotwater = st.number_input("Hot Water Heating (0=No, 1=Yes)", min_value=0, max_value=1, step=1)
aircondition = st.number_input("Air Conditioning (0=No, 1=Yes)", min_value=0, max_value=1, step=1)
parking = st.number_input("Parking", min_value=0, max_value=4, step=1)
prefarea = st.number_input("Preferred Area (0=No, 1=Yes)", min_value=0, max_value=1, step=1)
furniture = st.number_input("Furnishing Status(0,2)", min_value=0, max_value=2, step=1)

if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "area": [Area],
        "bedrooms": [Bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwater],
        "airconditioning": [aircondition],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus": [furniture]
    })

    # Convert all values to numeric
    input_data = input_data.astype(float)

    prediction = model.predict(input_data)[0]

    st.success(f"🏠 Predicted House Price: ₹{int(prediction):,}")
