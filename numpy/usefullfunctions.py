import numpy as np
a1 = np.array([2, 1, 3, 4])
a2 = np.arange(2, 10, 1)
a3 = np.ones((2,2,2))
a4 = np.eye(5)
a5 = np.ones((3, 3, 3))
print(a1.ndim) # dimension of the array
print(a3.shape) # shape
print(a4.size) # number of element
print(a2.dtype) # types of element
print(a2.itemsize) # size of element by bytes
print(a1.reshape(2,2)) # change shape of array
print(a3.reshape(1, -1))
# same method which does the samething but don't return anything
a3.resize(1, 6)
print(a3)

print(a5[0,:,:])# same result
print(a5[0,...])# with this inst
print(a5[1:3, 0, 1:3]) # same methods as a normal list
print(a5[1:3, :, 1:3])

c1 = np.arange(15)
b1 = c1 > 9 # Boolean value of each element (if > 9 = true)
print(b1) # can be usefull on assignements 

c1[b1] = 1 # Replace all the > 9 with 1  
print(c1) 

c2 = np.arange(25).reshape((5,5))
print(c2.max()) # max
print(c2.min()) # min
print(c2.sum()) # sum
print(c2.cumsum()) # array of sums (n + n-1) 
print(c2.max(axis = 0)) # max of each colomun
print(c2.max(axis=1)) # max each row
print(c1.cumsum(axis = 0))

# Shallow copy (copy with same memory address)
c3 = c2.copy() # create a copy of c2 on c3

# merge arrays
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(np.vstack((v1, v2))) # stack them verticaly
print(np.hstack((v1, v2))) # stack them horizontaly



















