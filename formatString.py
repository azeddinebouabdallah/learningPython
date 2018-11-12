print("Hello {0}, I have {1} you".format("Didou", "missed"))
print("Prices: {x}, {y}, {z}".format(x= 200, y = 240, z = 60))
print("Hello {user}, Today is {0} {1}".format(26, "October", user= "Didou"))

# Align test {:>spaces} or {:<spaces}.format()
print("{:<30}".format('Left alignment'))
print("{:>30}".format('Right alignment'))

#Binary format
print("{:b}".format(21))
#Hexadecimal format
print("{:x}".format(21))
#Octal format
print("{:o}".format(21))

# Format the string
print("""
	Hello {user},

			Welcome to this python program.
	""".format(user = "Didou"))