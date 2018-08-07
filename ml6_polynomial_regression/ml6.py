# Polinomial Regression
import pandas as pd
import numpy as np

dataset = pd.read_csv("D:\PycharmProjects\linear_algebra\ml6_polynomial_regression/Position_Salaries.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
print(np.shape(X))

print(np.shape(y))

# splitting the test
# from sklearn.model_selection import train_test_split
# X_train, y_train, X_test, y_test = train_test_split(X,y, test_size=0.2, random_state=0)


# encoding
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# labelencoder_X = LabelEncoder()
# X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
# onehotencoder = OneHotEncoder(categorical_features=[3])
# X = onehotencoder.fit_transform(X).toarray()
# print(X)


# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)

lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)

import matplotlib.pyplot as plt

plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title("True Salary or NOT (Linear Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show("12")


plt.scatter(X, y, color='red')
plt.plot(X, lin_reg2.predict(X_poly), color='blue')
plt.title("True Salary or NOT (Polynomial Regression)")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show("22")

lin_reg.predict(6.5)

lin_reg2.predict(poly_reg.fit_transform(6.5))