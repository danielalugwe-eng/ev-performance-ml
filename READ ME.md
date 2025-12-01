# ⚡ Electric Car Performance Prediction Project

## 📌 Overview

This project focuses on building a **machine learning system to predict electric car performance**, including metrics like acceleration, battery efficiency, driving range, or failure likelihood. The goal is to create a robust end-to-end pipeline that collects data, cleans it, trains models, evaluates performance, and deploys results through a FastAPI endpoint.

The project follows best practices in modular code design, experiment tracking, and deployment-ready machine learning systems.



## 🚗 Project Goals

* Predict key electric vehicle (EV) performance metrics.
* Analyze factors such as battery health, motor temperature, torque, load, environmental conditions, and driving behavior.
* Build models suitable for real-world EV analytics, fleet management, or predictive maintenance.
* Provide interpretable outputs to understand why a vehicle may underperform.

---

## 🧠 Key Features

* End-to-end ML pipeline: data → model → evaluation.
* Modular code structure for scalability and maintainability.
* Multiple machine learning algorithms: Random Forest, XGBoost, Neural Networks.
* Time-series and sensor-based EV telemetry support.
* Visual analytics: feature importance, error plots, correlations.

---

## 📂 Project Structure

```
ElectricCarPerformance/
│
├── data/
│   ├── raw/                 # Raw EV sensor or performance data
│   └── processed/           # Cleaned & prepared datasets
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_evaluation.ipynb
│
├── src/
│   ├── data_loader.py       # Loads & preprocesses datasets
│   ├── feature_engineering.py
│   ├── train.py             # Training scripts for ML models
│   ├── evaluate.py          # Evaluation & metrics
│   └── utils.py             # Helper functions
│
├── models/
│   └── saved_models/        # Exported trained models
│
├── api/
│   └── app.py               # FastAPI deployment endpoint
│
├── reports/
│   ├── figures/             # Plots & charts
│   └── final_report.pdf     # Project report
│
├── requirements.txt
└── README.md
```

---

## 🔧 Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ElectricCarPerformance.git
cd ElectricCarPerformance
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

* **Windows:** `venv\Scripts\activate`
* **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Data Description

EV telemetry typically includes:

* Voltage, current, and power draw
* Battery temperature and motor temperature
* State of Charge (SOC)
* Ambient temperature and humidity
* Vehicle speed and acceleration
* Torque and RPM
* Energy consumption per km

Predicted outputs can include:

* Estimated driving range
* Acceleration (0–60 mph)
* Battery degradation rate
* Motor overheating probability
* Maintenance or failure likelihood

---

## 🧪 Model Training

Train models using different algorithms:

```bash
python src/train.py --model random_forest
python src/train.py --model xgboost
python src/train.py --model lstm
```

Each training run logs:

* Training and validation metrics
* Loss curves
* Feature importance rankings

---

## 📈 Evaluation

Evaluation generates metrics and visualizations:

* RMSE, MAE, R²
* Confusion matrix (for classification)
* Feature importance charts
* Prediction vs actual plots

Run evaluation:

```bash
python src/evaluate.py --model models/saved_models/best_model.pkl
```

---

## 🛠 Feature Engineering

Common preprocessing steps:

* Handling missing sensor values
* Creating lag features for time-series
* Combining torque + RPM → power
* Scaling/normalization (MinMaxScaler or StandardScaler)
* Encoding categorical driving conditions

---

## 🚀 Deployment with FastAPI

The trained model is deployed through a FastAPI endpoint:

```bash
uvicorn api.app:app --reload
```

Example usage:

```python
from joblib import load
import requests

model = load("models/saved_models/best_model.pkl")

input_data = {
    "battery_temp": 32,
    "motor_temp": 75,
    "speed": 80,
    "current": 220,
    "voltage": 350
}

print(model.predict([list(input_data.values())]))
```

---

## 📘 Future Improvements

* Add deep learning models (GRU/LSTM) for sequential data
* Implement anomaly detection for rare EV faults
* Integrate real-time inference via MQTT/Kafka
* Build a dashboard for fleet performance insights

---

## 🙌 Acknowledgements

This project uses:

* Scikit-learn
* XGBoost
* PyTorch (optional for deep models)
* Pandas & NumPy
* Matplotlib & Seaborn
* FastAPI for deployment

---

## 🏁 Summary

This project provides a complete system for predicting electric car performance, including data processing, modeling, evaluation, and deployment through FastAPI. It is structured for technical audiences, GitHub sharing, or client demonstration.


