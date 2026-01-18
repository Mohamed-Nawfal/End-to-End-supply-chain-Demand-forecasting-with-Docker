# 📦 End-to-End Supply Chain Demand Forecasting

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://www.docker.com/)
[![Flask](https://img.shields.io/badge/API-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)

## 🚀 Project Overview
This project delivers a production-ready machine learning pipeline designed to forecast weekly retail sales. It bridges the gap between raw data science research and real-world deployment by containerizing a trained model into a scalable REST API.

### **The Business Problem**
Inaccurate demand forecasting leads to the "Bullwhip Effect," causing either excessive inventory costs or lost revenue due to stockouts. This project utilizes historical sales data, economic indicators (CPI, Fuel Price, Unemployment), and seasonal trends (Holidays) to provide accurate, actionable forecasts.

---

## 🛠️ Tech Stack & Architecture
* **Modeling:** Random Forest Regressor & XGBoost (Optimized using WMAE).
* **API Framework:** Flask (Python) for serving real-time predictions.
* **Containerization:** Docker (Standardizing the environment for any OS).
* **Data Engineering:** Pandas, NumPy, Scikit-Learn.
* **Environment:** Developed in Google Colab; Deployed via Docker Desktop.

---

## 📈 Key Results & Insights
* **Accuracy:** Achieved a **Weighted Mean Absolute Error (WMAE) of ~1,576**, significantly outperforming the baseline mean sales model.
* **Key Drivers:** Store Department, Store Size, and Weekly Seasonality were identified as the highest-impact features.
* **Performance:** Proved that Ensemble Tree-based methods (Random Forest) provided better stability for this tabular time-series data compared to Deep Learning (LSTM) approaches.

---


## Deployment with Docker
Ensure Docker Desktop is running on your machine.
#### Build the Docker image
```bash
docker build -t supply-chain-api .
```

####  Run the container (Maps local port 5000 to container port 5000)
```bash
docker run -p 5000:5000 supply-chain-api
```

## Testing the API
While the container is running, execute the provided test script in a separate terminal to receive a live prediction:
```bash
python test_api.py
```

## 📂 Project Structure
 * Final_Project.ipynb - Full data cleaning, EDA, and model training/validation.
 * supply_chain_forecast_api.py - Flask API script to handle POST requests and serve predictions.
 * Dockerfile - Configuration file to containerize the application environment.
 * requirements.txt - List of Python dependencies for the production environment.
 * test_api.py - Client-side script to verify API functionality and connectivity.

## 📜 License
Distributed under the MIT License. See LICENSE for more information.
Author: Mohamed Nawfal
Project: End-to-End Supply Chain and Demand Forecasting ML Deployment

