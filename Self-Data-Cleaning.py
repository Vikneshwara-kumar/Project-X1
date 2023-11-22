# Import the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


# Load the temperature sensor data into a Pandas DataFrame
data = pd.read_csv('temperature_data.csv')

# Preprocess the data (e.g. remove outliers, normalize the data, etc.)

# Remove outliers using the Z-score method
data = data[(data['Temperature'] - data['Temperature'].mean()) / data['Temperature'].std() < 3]

# Normalize the data using the Min-Max scaling method
scaler = MinMaxScaler()
data[['Temperature', 'Time']] = scaler.fit_transform(data[['Temperature', 'Time']])

# Choose the number of clusters to create
num_clusters = 3

# Initialize the K-means clustering algorithm
kmeans = KMeans(n_clusters=num_clusters)

# Fit the algorithm to the data
kmeans.fit(data)

# Get the cluster labels for each data point
labels = kmeans.labels_

print(data.size)
print(data)



# Visualize the clustering results
fig = plt.figure(figsize=(10, 7))
plt.scatter(data['Temperature'], data['Time'], c=labels, cmap='viridis')
plt.xlabel('Temperature')
plt.ylabel('Time')
plt.title('Temperature Sensor Data Clustering')
plt.show()
