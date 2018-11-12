"""
try:
	#instructions
except Exception1:
	#If there is exception type 1
except Exeption2:
	#If there is exception type 2
finally:
	#Finally instead of else
else: 
	#If there is no exceptions
"""
try : 
	a = 5 / 0
except ZeroDivisionError as e: 
	print ("Zero Division Error")
finally: 
	print ("Finish code")


# Throw an exception
def RaiseException(a):
	if type(a) != type('a'):
		raise Exception("a is not a string")
a = 1
try:
	RaiseException(a)
except Exception as e:
	print(e)

# One line throwing exception
def AssertException(a, b):
	assert a > b, "a is greater than b" # If not true throw an error

try :
	AssertException(2, 6)
except AssertionError as e:
	print (e)



