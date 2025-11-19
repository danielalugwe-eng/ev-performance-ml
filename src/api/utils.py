import os
import pickle
import pandas as pd
import logging

# -------------------
# Logger setup
# -------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ev_api")

# -------------------
# Load model + DictVectorizer once (Docker-compatible)
# -------------------
MODEL_PATH = os.path.join(os.path.abspath("/app/models"), "lasso_model.bin")

try:
    with open(MODEL_PATH, "rb") as f_in:
        dv, model = pickle.load(f_in)
    logger.info(f"Model loaded successfully from {MODEL_PATH}")
except FileNotFoundError:
    logger.error(f"Model file not found at {MODEL_PATH}")
    dv, model = None, None

# -------------------
# Prediction function
# -------------------
def predict_range(vehicle_dict: dict) -> float:
    """
    Given a dict of vehicle features, predict the range_km.
    """
    if dv is None or model is None:
        raise RuntimeError("Model not loaded. Cannot predict.")

    # Convert string values to lowercase
    for k, v in vehicle_dict.items():
        if isinstance(v, str):
            vehicle_dict[k] = v.lower()

    # Encode features
    X_encoded = dv.transform([vehicle_dict])

    # Predict
    y_pred = model.predict(X_encoded)
    return float(y_pred[0])
