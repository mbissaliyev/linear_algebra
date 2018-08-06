import numpy as np
import pandas as pd
import matplotlib as mp

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
y = np.reshape(y,(30,1))


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=0)

print(X)
print(y)

print("X train", X_train)
print("X test", X_test)
