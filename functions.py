def functionName(params, defaultArg = 10): 
	print (params)
	print (defaultArg)
	return 0


print (functionName("Didou"))
# Anonymous function
sum = lambda arg1, arg2 : arg1 + arg2

print (sum(10,10))

# Nested functions arguments
def f(a):
	def g(b):
		return a * b
	return g
print ("Nested functions : {0}".format(f(2)(6))) # Use double parentheses

# Nested lambda arguments
func = lambda a : lambda b: lambda c: a + b + c
print("Nested lambda functions: {0}".format(func(5)(5)(5)))
