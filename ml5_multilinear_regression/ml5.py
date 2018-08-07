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
y =dataset.iloc[:, 4].values

print(X[:,3])

# encoding states
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()
print(X)


