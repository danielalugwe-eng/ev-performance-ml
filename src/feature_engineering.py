import pandas as pd
from sklearn.feature_extraction import DictVectorizer
import pickle

# Load cleaned data
cleaned_path = r"C:\Users\user\electric_car_ml\data\processed\ev_cleaned.csv"
df = pd.read_csv(cleaned_path)

# Separate target
target = "range_km"
y = df[target]
X = df.drop(columns=[target])

# Convert to dict records
X_dict = X.to_dict(orient='records')

# Fit DictVectorizer
dv = DictVectorizer(sparse=False)
X_encoded = dv.fit_transform(X_dict)

# Save encoded features and vectorizer
X_encoded_path = r"C:\Users\user\electric_car_ml\data\processed\X_encoded.npy"
y_path = r"C:\Users\user\electric_car_ml\data\processed\y_target.npy"
dv_path = r"C:\Users\user\electric_car_ml\models\dv.bin"

import numpy as np
np.save(X_encoded_path, X_encoded)
np.save(y_path, y.values)

with open(dv_path, "wb") as f_out:
    pickle.dump(dv, f_out)

print("Feature engineering complete and DictVectorizer saved.")
