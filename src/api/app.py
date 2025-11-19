# src/api/app.py

from fastapi import FastAPI
from api.schemas import VehicleFeatures
from api.utils import logger, predict_range


app = FastAPI(title="Electric Car Prediction API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the EV Range Prediction API!"}


@app.post("/predict")
def predict(features: VehicleFeatures):
    """
    Receive a vehicle's features and return the predicted range_km.
    """
    vehicle_dict = features.model_dump()  # Convert Pydantic model to dict

    logger.info(f"Received request: {vehicle_dict}")

    try:
        predicted_range = predict_range(vehicle_dict)
        logger.info(f"Prediction success: range_km={predicted_range}")
        return {"predicted_range_km": predicted_range}

    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        return {"error": str(e)}
