# Chapter 5 - Data Visualization

import matplotlib.pyplot as plt
import numpy as np

# create plot

X = [x * 0.1 for x in range(100)]
y = np.sin(X)
plt.plot(X, y)

# save fig
plt.savefig("C:/Users/WIN10/PycharmProjects/linear_algebra/stats5/test.png")

# display plot
plt.show()

# bar chart
X = ['red', 'green', 'black']
y = [10, 20, 30]

plt.bar(X, y)
plt.show()

# histogram
X = np.random.randn(1000)
print(X)

plt.hist(X, bins=100)
plt.show()

# box and whisker plot

X = [np.random.randn(1000), 5*np.random.randn(1000), 10*np.random.randn(1000)]
plt.boxplot(X)
plt.show()

#scatter plot
x = 20 * np.random.randn(1000) + 100
y = x + (10* np.random.randn(1000) + 50)

plt.scatter(x,y)
plt.show()