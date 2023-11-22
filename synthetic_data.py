import numpy as np
from sklearn.linear_model import LinearRegression
import json
import csv
import time

# Generate some training data
x_train = np.random.rand(1000, 1) * 100
y_train = 20 + 0.5 * x_train + np.random.randn(1000, 1) * 10

# Train a linear regression model on the training data
model = LinearRegression().fit(x_train, y_train)

# Generate some test data
x_test = np.random.rand(100, 1) * 100

# Use the trained model to generate synthetic temperature data
y_test = model.predict(x_test)

# Get the current time in seconds since the epoch
current_time = time.time()

# Create a list to store the temperature data with timestamps
temperature_data = []

# Loop over the test data and append each predicted temperature value
# with a corresponding timestamp to the temperature_data list
for i in range(len(y_test)):
    timestamp = current_time + i * 60  # Add one minute to the timestamp for each data point
    temperature_data.append({"timestamp": timestamp, "temperature": float(y_test[i])})

# Serialize the temperature data to JSON format
json_str = json.dumps(temperature_data)

# Write the JSON data to a file
with open("temperature_data.json", "w") as f:
    f.write(json_str)
