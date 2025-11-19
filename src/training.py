import pickle
import numpy as np
from sklearn.linear_model import Lasso

# Paths
X_path = r"C:\Users\user\electric_car_ml\data\processed\X_encoded.npy"
y_path = r"C:\Users\user\electric_car_ml\data\processed\y_target.npy"
dv_path = r"C:\Users\user\electric_car_ml\models\dv.bin"
model_path = r"C:\Users\user\electric_car_ml\models\lasso_model.bin"

# Load features, target, and vectorizer
X_encoded = np.load(X_path)
y = np.load(y_path)

with open(dv_path, "rb") as f_in:
    dv = pickle.load(f_in)

# Train Lasso
model = Lasso(alpha=0.1, max_iter=10000)
model.fit(X_encoded, y)

# Save model (can save dv separately or together)
with open(model_path, "wb") as f_out:
    pickle.dump((dv, model), f_out)

print(f"Model trained and saved to {model_path}")
