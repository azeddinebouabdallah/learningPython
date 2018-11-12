# Data strecture Listes

l = ["Bouabdallah Azeddine", "Bouabdallah Younes", "Bouabdallah Sara"]
print (l)

# Add element
l += ["Bouabdallah Abd El Majid", "Benabess Mekia"]
print (l)

# Append 
l.append("Benabess Ounassa")
print(l)

# Contain
print ("Bouabdallah Azeddine" in l)

# Compaire 
print (l == ["Whatever!"])

# List functions
# map(function, list)  : the function takes param (element of the list) and do whatever you wanna do
# list() = type casting
print(list(map(lambda element : element ** 2, [1, 2, 3, 4])))

# filter(function, list) : function serves as condition.
print(list(filter(lambda element: element > 4, [1, 5, 3, 7])))

# reduce(function, list) : return only one result
# you need to import functools
import functools

print(functools.reduce(lambda x, y : x + y , [1, 2, 3, 4]))