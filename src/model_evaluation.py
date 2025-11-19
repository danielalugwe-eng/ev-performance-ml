import pickle
import numpy as np
from sklearn.metrics import mean_squared_error

# Paths
X_path = r"C:\Users\user\electric_car_ml\data\processed\X_encoded.npy"
y_path = r"C:\Users\user\electric_car_ml\data\processed\y_target.npy"
model_path = r"C:\Users\user\electric_car_ml\models\lasso_model.bin"

# RMSE function
def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

# Load test data
X_test = np.load(X_path)
y_test = np.load(y_path)

# Load model + dv
with open(model_path, "rb") as f_in:
    dv, model = pickle.load(f_in)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Test RMSE:", rmse(y_test, y_pred))
