# 📦 End-to-End Supply Chain Demand Forecasting


## 🚀 Project Overview
This project delivers a production-ready machine learning pipeline for forecasting weekly retail sales. It bridges the gap between raw data science research and software deployment by containerizing a trained model into a scalable REST API.



### **The Challenge**
Supply chain managers face the "Bullwhip Effect" where inaccurate demand forecasts lead to overstocking or stockouts. This project uses historical sales data, seasonal trends (Holidays), and economic indicators (CPI, Unemployment) to predict demand with high precision.

---

## 🛠️ Tech Stack & Architecture
* **Modeling:** Random Forest Regressor & XGBoost (Optimized via WMAE)
* **API Framework:** Flask (Python)
* **Containerization:** Docker
* **Environment:** Google Colab (Research) & Local Desktop (Deployment)
* **Data Engineering:** Pandas, NumPy, Scikit-Learn

---

## 📈 Key Results
* **Accuracy:** Achieved a **Weighted Mean Absolute Error (WMAE) of ~1,576**, representing a significant improvement over baseline seasonal averages.
* **Top Features:** Store Department, Store Size, and Weekly Seasonality were identified as the primary drivers of sales.
* **Architecture:** Proved that Ensemble Tree methods outperformed LSTM architectures for this specific tabular time-series dataset.

---

## Deployment with Docker
'''
docker build -t supply-chain-api .
docker run -p 5000:5000 supply-chain-api
'''
