import pandas as pd
import pickle

# Paths
model_path = r"C:\Users\user\electric_car_ml\models\lasso_model.bin"
test_path = r"C:\Users\user\electric_car_ml\data\processed\ev_cleaned.csv"
pred_path = r"C:\Users\user\electric_car_ml\data\predictions\ev_predictions.csv"

# Load model + dv
with open(model_path, "rb") as f_in:
    dv, model = pickle.load(f_in)

# Load new data
df_test = pd.read_csv(test_path)

# Drop target if exists
target_col = 'range_km'
if target_col in df_test.columns:
    X_test = df_test.drop(columns=[target_col])
else:
    X_test = df_test.copy()

# Convert strings to lowercase
str_cols = X_test.select_dtypes(include='object').columns
for col in str_cols:
    X_test[col] = X_test[col].str.lower()

# Encode features
X_test_encoded = dv.transform(X_test.to_dict(orient="records"))

# Predict
y_pred = model.predict(X_test_encoded)

# Save predictions
df_test['predicted_range_km'] = y_pred
df_test.to_csv(pred_path, index=False)
print(f"Predictions saved to {pred_path}")

# Optional: compute RMSE if target exists
if target_col in df_test.columns:
    from sklearn.metrics import mean_squared_error
    import numpy as np
    print("Test RMSE:", np.sqrt(mean_squared_error(df_test[target_col], y_pred)))
