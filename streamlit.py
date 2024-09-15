import streamlit as st
import numpy as np
import pandas as pd
import datetime
import xgboost as xgb

import joblib

# Initialize the current date
date_time = datetime.datetime.now()

# Load the XGBoost model
model = xgb.XGBRegressor()
model.load_model('xgb_model.json')

def main():
    # Set the page configuration and background
    st.set_page_config(page_title="Car Price Prediction", layout="centered")

    # Add custom CSS to enhance UI
    st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 6px 12px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        .stSelectbox select {
            width: 50%;
            padding: 6px 10px;
            margin: 4px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 2px;
            box-sizing: border-box;
        }
    </style>
    """, unsafe_allow_html=True)

    # Create the title banner
    html_temp = """
    <div style = " background: linear-gradient(90deg, rgba(255, 87, 34, 1)0%, rgba(54, 69, 79, 1) 100%);background-color:#1F77B4;padding:2px;border-radius:14px;">
    <h1 style="color:white;text-align:center;"> Car Price Prediction Using Machine Learning</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Display some introductory text
    st.markdown("""
    <div style="text-align: center;">
        <h3>Are you planning to sell your car 🚗?</h3>
        <h4>Let's estimate the potential price of your car with advanced machine learning techniques.</h4>
    </div>
    """, unsafe_allow_html=True)

    
    st.write('---')  # Horizontal line
    
    # Input fields for the car details
    col1, col2 = st.columns(2)
    with col1:
        p1 = st.number_input('🔢 Ex-showroom price of the car (in Lakhs)', 2.5, 25.0, step=0.5) 
    with col2:
        p2 = st.number_input('📏 Distance completed by the car (in Kilometers)', 100, 500000, step=1000)
    
    s1 = st.selectbox('⛽ Fuel Type', ('Petrol', 'Diesel', 'CNG'))
    p3 = 0 if s1 == "Petrol" else 1 if s1 == "Diesel" else 2
    
    s2 = st.selectbox('🧑‍💼 Are you a dealer or an individual?', ('Dealer', 'Individual'))
    p4 = 0 if s2 == "Dealer" else 1
    
    s3 = st.selectbox('⚙️ Transmission Type', ('Manual', 'Automatic'))
    p5 = 0 if s3 == "Manual" else 1
    
    p6 = st.slider("👥 Number of previous owners", 0, 3)
    
    years = st.number_input('📅 Year the car was purchased', 1990, date_time.year, step=1)
    p7 = date_time.year - years
    
    # Prepare the input data for the model
    data_new = pd.DataFrame({
        'Present_Price': [p1],
        'Kms_Driven': [p2],
        'Fuel_Type': [p3],
        'Seller_Type': [p4],
        'Transmission': [p5],
        'Owner': [p6],
        'Age': [p7]
    })
    
    # Add a button for predictions
    if st.button('🔎 Predict Car Price'):
        try:
            prediction = model.predict(data_new)
            if prediction > 0:
                st.balloons()
                st.success(f'🎉 You can sell the car for **₹{prediction[0]:.2f} Lakhs**.')
            else:
                st.warning("😕 The car may not be suitable for sale at the moment.")
        except:
            st.error("⚠️ Something went wrong! Please check the inputs and try again.")

# Run the main function
if __name__ == '__main__':
    main()
