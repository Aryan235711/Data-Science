"""Linear Regression model which creates a regressor"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

# Load the diabetes dataset
# This dataset contains ten baseline variables (features) collected from diabetes patients, used to predict disease progression.
diabetes = datasets.load_diabetes()

# Extract a single feature (Body Mass Index - BMI) for simplicity in visualization and training
# diabetes.data[:, np.newaxis, 2] selects the third feature and reshapes it into a column vector.
diabetes_X = diabetes.data[:, np.newaxis, 2]
"""
Explanation--

diabetes.data[:, np.newaxis, 2]:----
-->: means “all elements” along the first axis.
-->np.newaxis adds a new dimension (or axis) at that position.
-->2 selects the third column (index 2, since Python is 0-indexed) from the array.
This will extract the third column of diabetes.data and insert a new axis, changing its shape.

For example, if diabetes.data originally has the shape (442, 10), then after indexing with [:, np.newaxis, 2] the shape will be (442, 1) 
(assuming you want a 2D column vector).

"""

# Splitting dataset into training and testing sets
# The first 412 samples (442-30) are used for training
# The last 30 samples are used for testing

diabetes_X_train = diabetes_X[:-30]  # Training data (features)
diabetes_X_test = diabetes_X[-30:]   # Testing data (features)

diabetes_y_train = diabetes.target[:-30]  # Training data (labels)
diabetes_y_test = diabetes.target[-30:]   # Testing data (labels)

# Create a linear regression model
model = linear_model.LinearRegression()

# Train the model using training data
model.fit(diabetes_X_train, diabetes_y_train)

# Predict the target values for test data
diabetes_y_predict = model.predict(diabetes_X_test)

# Evaluate the model performance using Mean Squared Error (MSE)
# MSE measures the average squared difference between actual and predicted values (lower values indicate better performance)
print("The mean squared error is:", mean_squared_error(diabetes_y_test, diabetes_y_predict))

# Display the learned parameters
print("Weights (Coefficient) :", model.coef_)  # The slope of the regression line (effect of BMI on disease progression)
print("Intercept :", model.intercept_)  # The y-intercept (where the line crosses the y-axis when BMI is zero)

# Visualization of the regression line
plt.scatter(diabetes_X_test, diabetes_y_test, color='blue', label='Actual Data')  # Scatter plot of actual test data
plt.plot(diabetes_X_test, diabetes_y_predict, color='red', linewidth=2, label='Predicted Regression Line')  # Regression line
plt.xlabel("BMI")
plt.ylabel("Disease Progression")
plt.title("Linear Regression on Diabetes Dataset")
plt.legend() #A legend in a plot is a small box that explains what different elements in the graph represent. It helps in understanding the meaning of colors, markers, and lines used in a visualization.
plt.show()

