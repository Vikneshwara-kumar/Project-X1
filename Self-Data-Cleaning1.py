# Import the required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load the temperature sensor data into a Pandas DataFrame
data = pd.read_csv('temperature_data.csv')

# Preprocess the data (e.g. remove outliers, normalize the data, etc.)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[['Temperature', 'Time']], test_size=0.2, random_state=42)

# Initialize the SVM classifier
clf = SVC(kernel='linear')

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Predict the classes for the testing data
y_pred = clf.predict(X_test)

# Evaluate the performance of the classifier
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
