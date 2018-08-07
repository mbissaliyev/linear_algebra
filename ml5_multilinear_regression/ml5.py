# Multilinear regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("D:\PycharmProjects\linear_algebra\ml5_multilinear_regression/50_startups.csv")

print(dataset)

A = np.array(dataset)

# RND = dataset.iloc[:, :1].values
# ADM = dataset.iloc[:, 1:2].values
# MARKETING = dataset.iloc[:, 2:3].values
# STATE = dataset.iloc[:, 3:4].values

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# encoding states
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()
print(X)

# avoiding dummy variable trap
X = X[:, 1:]

# split Test and Train set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# fit multiple regression to the training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting the test set results
y_pred = regressor.predict(X_test)
# y_pred = np.reshape(y_pred,(10,1))


# backward elimination
import statsmodels.formula.api as sm

X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 1,  3, 4, 5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

# Conclusion: companies that spent more money on R&D have more profit