# Shallow copy 
# Shallow copy = 2 copies of a 
# share the same set of elements. same pointer
import copy

myList = [1, 2, 3]
myList2 = myList

print(myList)
myList[1] = 10
print(myList2)

myList = [1, 2, 3] 
myList2 = copy.deepcopy(myList) # To prevent sharing same set
print(myList)
myList[1] = 10
print(myList2)
