# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
# =============================================================================
# from sklearn.cross_validation import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# =============================================================================

#Fitting linear regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

#Fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly,y)

#Visulazing the linear regression results
plt.scatter(X,y,color = 'red')
plt.plot(X,lin_reg.predict(X),color = 'blue')
plt.title("Truth or bluff (Linear regression)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()

#Visulazing the polynomial linear regression results
X_grid = np.arange(min(X),max(X),0.1)
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color = 'red')
plt.plot(X_grid,lin_reg2.predict(poly_reg.fit_transform(X_grid)),color = 'blue')
plt.title("Truth or bluff (Polynomial regression)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()

#Predicting the result with linear regression
arr = np.array([6.5]).reshape(1,-1)
lin_reg.predict(arr)

#Predicting the result with Polynomial regression
lin_reg2.predict(poly_reg.fit_transform(arr))
