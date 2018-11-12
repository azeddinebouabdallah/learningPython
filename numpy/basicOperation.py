import numpy as np

x = np.linspace(0, 6.28, 20)
print(np.sin(x))# Sin of each element
print(np.cos(x)) # cos
print(np.tan(x)) # Tng

x = np.arange(9).reshape(3, 3)
print(x > 4) # boolean values of this conditions
print(x < 4)

print(x**2) # raise each element 
print(np.exp(x)) # e
print(x * 4) # each element by 4
print(x - 4) 

y = np.arange(10, 19).reshape(3, 3)

print(x*y) # (1,1)*(1,1) ... etc

# if arrays are not the same size => (But fist must x of a = y of b)
a = np.array([[1,1], [2,2], [3,3]]) # x of a = 2
b = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) # y of b = 2
# 2 = 2
print(a.dot(b))
# OR
print(np.dot(a, b))