import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Load the temperature sensor data into a Pandas DataFrame
data = pd.read_csv('temperature_data.csv')

# Preprocess the data (e.g. remove outliers, normalize the data, etc.)
data = data[(data['Temperature'] - data['Temperature'].mean()) / data['Temperature'].std() < 3]

# Normalize the data using the Min-Max scaling method
scaler = MinMaxScaler()
data[['Temperature', 'Time']] = scaler.fit_transform(data[['Temperature', 'Time']])

# Choose the number of clusters to create
num_clusters = 5

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


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[['Temperature']], data['Time'], test_size=0.2, random_state=42)

# Define the neural network architecture
model = Sequential()
model.add(Dense(64, input_shape=(1,), activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
model.compile(loss='mean_squared_error', optimizer=Adam(0.001))

# Define early stopping criteria
early_stopping = EarlyStopping(monitor='val_loss', patience=5)

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=32, callbacks=[early_stopping], shuffle=True)

# Evaluate the performance of the model on the testing data
loss = model.evaluate(X_test, y_test)
print('Test loss:', loss*100)
