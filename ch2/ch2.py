import numpy as np

#creating 1D array
a = [1,2,3]


a = np.array(a)
print(a)
print(a.shape)

#importing csv
import pandas as pd

data = pd.read_csv("data.csv")

#converting to 2D array
data = np.array(data)
print(data)


