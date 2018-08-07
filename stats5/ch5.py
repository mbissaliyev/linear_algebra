# Chapter 5 - Data Visualization

import matplotlib.pyplot as plt
import numpy as np

# create plot

X = [x * 0.1 for x in range(100)]
y = np.sin(X)
plt.plot(X, y)

#save fig
plt.savefig("C:/Users/WIN10/PycharmProjects/linear_algebra/stats5/test.png")

# display plot
plt.show()
