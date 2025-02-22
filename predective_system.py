# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import pickle
import sklearn

#loading the saved model
loaded_model = pickle.load(open('C:/Users/gowri/OneDrive/Desktop/model/trained_model.sav', 'rb'))

def predict_car_price(year, present_price, kms_driven, fuel_type, seller_type, transmission, owner):
    # Load the trained model

    # Encode categorical features
    fuel_type_encoded = 0 if fuel_type == "Petrol" else 1 if fuel_type == "Diesel" else 2
    seller_type_encoded = 0 if seller_type == "Dealer" else 1
    transmission_encoded = 0 if transmission == "Manual" else 1

    # Calculate the car's age
    current_year = 2024  
    age = current_year - year

    # Create input array for prediction
    features = np.array([[age, present_price, kms_driven, fuel_type_encoded, seller_type_encoded, transmission_encoded, owner]])
    predicted_price = loaded_model.predict(features)
    print(f"Predicted Selling Price: ₹{predicted_price[0]:.2f} lakhs")


# Example usage
predict_car_price(
    year=2014,
    present_price=10.5,
    kms_driven=510,
    fuel_type="Petrol",
    seller_type="Dealer",
    transmission="Manual",
    owner=0
)

