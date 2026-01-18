FROM python:3.9-slim
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your specific files
COPY supply_chain_rf_model.pkl .
COPY supply_chain_forecast_api.py .

# Expose port 5000 for the API
EXPOSE 5000

# Tell Docker to run your NEW filename
CMD ["python", "supply_chain_forecast_api.py"]
