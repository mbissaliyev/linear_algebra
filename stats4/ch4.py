# chapter 4 Gaussian Distribution

import numpy as np
from matplotlib import pyplot
from scipy.stats import norm

X_axis = np.arange(-3, 3, 0.001)

y_axis = norm.pdf(X_axis, 0, 1)

# pyplot.plot(X_axis,y_axis)
# pyplot.show()

# test dataset

np.random.seed(1)
data = 5 * np.random.randn(10000) + 50
print(data)

# pyplot.hist(data,bins=100)
# pyplot.show()

result = np.mean(data)
print("Mean %.3f" % result)
print("Median %.3f" % np.median(data))


#pyplot.plot(X_axis, norm.pdf(X_axis,0,0.5))
#pyplot.plot(X_axis, norm.pdf(X_axis,0,1))
#pyplot.show()

result = np.var(data)
print(result)

stddev = np.std(data)
print("Standard deviation %.3f" %stddev)
