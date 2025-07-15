import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
# %matplotlib inline
# Creating a non linear function 
np.random.seed(23)
noise = np.random.randn(100,1)
x = 5 * np.random.rand(100,1) - 2
y = 7*x**2 + 4*x + 7 + noise
y.shape,x.shape
# Lets plot the graph to see the non linear function
plt.scatter(x=x,y=y, edgecolors='black')
plt.show()
# Now lets quickly split the data into training and testing part
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=23)
x_train.shape, x_test.shape, y_train.shape, y_test.shape
# Now lets apply polynomial transformation similar to StandardScalar
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=True)
x_poly_train = poly.fit_transform(x_train)
x_poly_test = poly.transform(x_test)
# Importing the regressor model for polynomial transformation
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(x_poly_train,y_train)
# Now checking how the model is looking over the given datapoints
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x_train, y_train)
plt.scatter(x_train, reg.predict(x_poly_train), c = 'red')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.show()
# Now lets predict the values with the help of model
y_pred = reg.predict(x_poly_test)
y_pred.shape
# Now lets check the metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score
# Calculate predictions (assuming y_test and y_pred are already available)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)  # Manual computation
r2 = r2_score(y_test, y_pred)

# Display results
print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R² Score: {r2}")
# Lets use cross-validation to see the model is not overfitting
from sklearn.model_selection import cross_val_score
validation = cross_val_score(estimator=reg, X=x_poly_train, y=y_train, cv=5, scoring='r2' )
np.mean(validation)
# Using OLS 
import statsmodels.api as sm
ols_model = sm.OLS(y_train, x_poly_train).fit()
ols_y_pred = ols_model.predict(x_poly_test)
ols_model.summary()
# Now lets try to predict using new set of data
x_new = np.linspace(start=-3,stop=3,num=200).reshape(200,1)
x_new_poly = poly.transform(x_new)
y_new_pred = reg.predict(x_new_poly)
plt.plot(x_train, y_train)
plt.plot(x_new, y_new_pred)
plt.show()