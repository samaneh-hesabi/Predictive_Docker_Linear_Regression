import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
print("Loading the salary dataset...")
file_path = 'Salary_Data.csv'
data = pd.read_csv(file_path)

# Data processing
print("Preparing data for training...")
X = data[['YearsExperience']]
y = data['Salary']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
print("Training the linear regression model...")
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
print("Evaluating the model...")
y_pred = model.predict(X_test)

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error on test set: {mse:.2f}")
print(f"R-squared on test set: {r2:.2f}")

# Save the model coefficients
print("Saving the model...")
with open('model_coefficients.pkl', 'wb') as f:
    pickle.dump(model.coef_, f)

# Predict on unknown data
print("\nMaking predictions for new data...")
# Example unknown data
unknown_data = np.array([[5], [10], [15]])  # Years of experience
predictions = model.predict(unknown_data)

# Output predictions
for i, prediction in enumerate(predictions):
    print(f"Prediction for {unknown_data[i][0]} years of experience: ${prediction:.2f}")

print("\nDone! The model has been trained and saved.") 