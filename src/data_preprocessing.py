import pandas as pd

# Load raw data
raw_path = r"C:\Users\user\electric_car_ml\data\raw\electric_vehicles_spec_2025.csv.csv"
df = pd.read_csv(raw_path)

# Drop missing values
df = df.dropna()

# Convert all string columns to lowercase
str_cols = df.select_dtypes(include='object').columns
for col in str_cols:
    df[col] = df[col].str.lower()

# Save cleaned data
cleaned_path = r"C:\Users\user\electric_car_ml\data\processed\ev_cleaned.csv"
df.to_csv(cleaned_path, index=False)
print(f"Cleaned data saved to {cleaned_path}")
