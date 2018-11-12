# Data Strecture Tuple

tup = ("Bouabdallah Azeddine","Bouabdallah Younes","Bouabdallah Sara")
tup1 = 100, 300, 200
tup2 = ('A')

print (tup[1:])
print (tup1)
print(tup2)

try: 
	tup[0] = "Bouabdallah None"
except Exception as e:
	print (e)

# Add element to the end
tup = tup + ("Bouabdallah Abd El Majid", "Benabess Mekia")
print (tup)

# Contain element
print ("Bouabdallah Azeddine" in tup)

for user in tup: 
	print (user)

# Useful function 
print (len(tup)) # Length of a tuple
print (max(tup1)) # Max element in a tuple
print (min(tup1)) # Min element inf a tuple