from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# 1. Load the winning Random Forest model we saved earlier
model = pickle.load(open('supply_chain_rf_model.pkl', 'rb'))

# Define the feature columns and their order, exactly as used during training
# This list comes from X.columns = df.drop(['Weekly_Sales', 'Date'], axis=1).columns
FEATURE_COLUMNS = ['Store', 'Dept', 'IsHoliday', 'Type', 'Size', 'Temperature', 'Fuel_Price',
                   'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5', 'CPI',
                   'Unemployment', 'Year', 'Month', 'Week', 'Day']

# 2. Add a 'Home' route so you can see something in your browser
@app.route('/')
def home():
    return "<h1>Supply Chain Sales Prediction API</h1><p>The server is running! Use the /predict endpoint to get forecasts.</p>"

# 3. Add the Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the POST request
        data = request.get_json()

        # Convert JSON input into a DataFrame
        input_df = pd.DataFrame([data])

        # Ensure column order matches the model training order
        # Any missing columns will be filled with NaN, and extra columns dropped
        input_df = input_df[FEATURE_COLUMNS]

        prediction = model.predict(input_df)

        return jsonify({
            'status': 'success',
            'predicted_weekly_sales': round(float(prediction[0]), 2)
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    # We set debug=False for production readiness
    app.run(host='0.0.0.0', port=5000)
