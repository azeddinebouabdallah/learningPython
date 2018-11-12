# To prevent 2 data strectures from sharing the same set you must use this
mySet = set([1, 2, 3])
mySet1 = set([4, 5, 1])
print(mySet)
print(mySet1)

# Sets functions
# union
print (set.union(mySet, mySet1))
# intersection
print(set.intersection(mySet, mySet1))