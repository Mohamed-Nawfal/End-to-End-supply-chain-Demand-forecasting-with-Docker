import requests

# The URL of your local Docker container
url = 'http://127.0.0.1:5000/predict'

# Data for one specific week/store (Example)
data = {
    "Store": 1,
    "Dept": 1,
    "Type": 1,
    "Size": 151315,
    "Temperature": 42.31,
    "Fuel_Price": 2.572,
    "MarkDown1": 0.0,
    "MarkDown2": 0.0,
    "MarkDown3": 0.0,
    "MarkDown4": 0.0,
    "MarkDown5": 0.0,
    "CPI": 211.09,
    "Unemployment": 8.106,
    "IsHoliday": 0,
    "Year": 2012,
    "Month": 11,
    "Week": 44,
    "Day": 2
}

# Send the data to Docker
response = requests.post(url, json=data)

# See the result!
print("Status Code:", response.status_code)
print("Prediction Result:", response.json())