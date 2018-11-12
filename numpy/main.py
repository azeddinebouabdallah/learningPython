# Numpy
import numpy as np

array1 = np.array([2, 1, 3, 4]) # Creating the array
array2 = np.array([[1, 2, 1], [2, 1, 2], [1,2,3]]) # 2D array
array3 = np.array([[[1, 2, 3], [3, 2, 1]],[[4, 5, 6], [6, 5, 4]]])
print(array1)
print(array2)
print(array3)

array4 = np.arange(10, 50, 1) # start, end, steps, type
# Create array that starts from 10 and ends in 50 with 1 step
array5 = np.arange(10)
array6 = np.arange(0.3, 2, 0.2)
print(array4)
print(array5)
print(array6)

#linspace
array7 = np.linspace(3, 8, 9) # starts, end, number of steps
print(array7)

#Multi demintions array with specific type
array8 = np.ones((2,2,2)) # 2 x, 2y, 2z create array with all ones
print(array8)

array9 = np.zeros((2, 2, 2)) # with all zeros
print(array9)

array10 = np.empty((2,2,2)) # with random data
print(array10)

array11 = np.eye(5) # matrix with this size
print(array11)

array12 = np.random.random((5,5)) # random data for specific matrix











