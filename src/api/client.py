import requests

# URL of your running FastAPI server
API_URL = "http://127.0.0.1:8000/predict"

# Example payload with realistic EV features
payload = {
    "brand": "tesla",
    "model": "model s",
    "top_speed_kmh": 250,
    "battery_capacity_kWh": 100,
    "battery_type": "li-ion",
    "number_of_cells": 8000,
    "torque_nm": 700,
    "efficiency_wh_per_km": 180,
    "acceleration_0_100_s": 3.2,
    "towing_capacity_kg": 500,
    "cargo_volume_l": 850,
    "seats": 5,
    "drivetrain": "AWD",
    "segment": "luxury",
    "length_mm": 4970,
    "width_mm": 1960,
    "height_mm": 1440,
    "car_body_type": "sedan",
    "source_url": "https://example.com"
}

response = requests.post(API_URL, json=payload)

if response.status_code == 200:
    print("Predicted Range (km):", response.json()["predicted_range_km"])
else:
    print("Error:", response.json())
