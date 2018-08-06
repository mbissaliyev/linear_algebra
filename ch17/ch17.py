# Chapter 17 - Multivariate Statistics
import numpy as np

v = np.array([1, 2, 3, 4, 5, 6])

print(v)

result = np.mean(v)
print(result)

M = np.array([
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]

])

col_mean = np.mean(M, axis=0)
print(col_mean)

row_mean = np.mean(M, axis=1)
print(row_mean)

# variance

v = np.array([1, 2, 3, 4, 5, 6])

result = np.var(v, ddof=1)
print(result)

M = np.array([
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]])
print(M)
# column standard deviations
col_std = np.std(M, ddof=1, axis=0)
print(col_std)
# row standard deviations
row_std = np.std(M, ddof=1, axis=1)
print(row_std)

#covariance

x = np.array([1,2,3,4,5,6,7,8,9])
print(x)

y = np.array([9,8,7,6,5,4,3,2,1])
print(y)

Sigma = np.cov(x,y)[0,1]
print(Sigma)


corr = np.corrcoef(x,y)[0,1]
print(corr)


#covariance matrix
# covariance matrix
from numpy import array
from numpy import cov
# define matrix of observations
X = array([
[1, 5, 8],
[3, 5, 11],
[2, 4, 9],
[3, 6, 10],
[1, 5, 10]])
print(X)
# calculate covariance matrix
Sigma = cov(X.T)
print(Sigma)

