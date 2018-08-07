import numpy as np
import pandas as pd
import matplotlib.pyplot as mp

# load data set
dataset = pd.read_csv("D:\PycharmProjects\linear_algebra\ml4_regression\Salary_Data.csv")

# print(dataset)

# simple linear regression t = b0 + b1*x1
# y = Dependent Variable (DV)
# x = Independent Variable (IV)
# b = coefficients


A = np.array(dataset)
print(A)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
y = np.reshape(y, (30, 1))

# split dataset
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)

# X_train = train_test_split(X,y, test_size=1/3, random_state=0)


print(X)
print(y)

print("X train", X_train)
print("X test", X_test)

# feature scaling

# fit linear regression to training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting test result
y_pred = regressor.predict(X_test)

print(y_pred)

# Plotting the Training set results
mp.scatter(X_train, y_train, color='red')
mp.plot(X_train, regressor.predict(X_train), color='blue')
mp.title("Salary vs Experience (Training Set)")
mp.xlabel("Years of Experience")
mp.ylabel("Salary")
mp.show()

# Plotting the Test results
mp.scatter(X_test, y_test, color='green')
mp.plot(X_train, regressor.predict(X_train), color='blue')
mp.title("Salary vs Experience (Test Set)")
mp.xlabel("Years of Experience")
mp.ylabel("Salary")
mp.show()
