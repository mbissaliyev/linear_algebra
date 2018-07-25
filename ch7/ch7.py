# ch7 - vectors

# v = (v1,v2,v3) - horizontal representation

#     (v1)
#     (v2)
# v = (v3) - vertical representation
#     (v4)
#     (v5)


import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([1, 2, 3])
print(b)

# addition
c = a + b
print(c)

# substraction
d = a - b
print(d)

# multiplication
v = a * b
print(v)

# division
dd = a / b
print(dd)

# vector scalar multiplication
a = np.array([1, 2, 3])
print(a)

b = np.array([3, 4, 5])
print(b)

c = a.dot(b)

# c = a1*b1 + a2*b2 + a3*b3
# c = 3 + 8 + 15


print(c)
