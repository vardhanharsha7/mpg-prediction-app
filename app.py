import streamlit as st
import pickle
import numpy as np

# Load trained model
with open('mpg.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("MPG Prediction App 🚗")

st.markdown("""
Predict the **Miles Per Gallon (MPG)** of a car based on its specifications.
""")

# User inputs
cylinders = st.selectbox(
    'Select Number of Cylinders',
    options=[3, 4, 5, 6, 8],
    index=1
)

horsepower = st.number_input(
    'Horsepower',
    min_value=40,
    max_value=250,
    value=100
)

displacement = st.number_input(
    'Displacement',
    min_value=50,
    max_value=500,
    value=150
)


# Prediction button
if st.button('Predict MPG'):
    # Prepare input array for model
    input_data = np.array([[cylinders, horsepower, displacement]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted MPG: {prediction:.2f}")
