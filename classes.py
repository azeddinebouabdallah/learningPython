class Employee(object): # object father class of all classes, allow us to override property function
	# Documentation of the class
	'This class simulate the Employee'
	#Class variable
	empCount = 0

	#Private variable
	__code = 10 # Use setters and getters

	#Constructor	
	def __init__(self, name, salary = 0): 
		# Control data type 
		if (type(name) != str ) and (type(salary) not in (int, float)):
			raise Exception("Arguments type errors {0}".format(self))
		self.name = name
		self.salary = salary
		self.__privateVar = "Whatever"
		Employee.empCount += 1
	
	#Add self to indicate this obj like this. in java
	def displayCount(self):
		print("Total Employee %d" % Employee.empCount)

	def displayEmployee(self):
		print ("Name: ", self.name, ", Salary: ", self.salary, "Code: ", self.__code )

	# To String function
	def __str__(self): # toString function
		return self.name + ' : ' + str(self.salary) 	
	# Addition of class 
	def __add__(self, other): 
		return Employee(self.name + " + " + other.name, self.salary + other.salary)
	#Multiplaction of class
	def __mul__(self, other):
		return Employee(self.name + " * " + other.name, self.salary * other.salary)
	# True division = __mod__ __truediv__
	def __div__(self, other):
		return Employee(self.name + " / " + other.name, self.salary / other.salary)

	# Abstractions for functions
	countDisplay = property(displayCount)
	userDisplay = property(displayEmployee)

# You can use multiple inheritance
class HardWorkerEmployee(Employee): 
	def hardWorkingMode(self):
		print ("Hard working mode active")
	def __str__(self): 
		return self.name + ' : ' + str(self.salary) + '. He is a hard-worker'

# Create objects
try: 
	emp1 = HardWorkerEmployee("Didou", 2000)
	emp2 = Employee("Houda", 2)
	emp1.displayCount()
	emp2.displayCount()
	emp1.displayEmployee()
	emp2.displayEmployee()
	print("Total Employee %d", Employee.empCount)
	emp1.hardWorkingMode()
	print (emp1.__str__())
	print (emp2.__str__())
	print("#"*12)
	print(emp1 + emp2) # Addition of class
	print(emp1 * emp2) # mult of class
	print((emp1 / emp2)) # Division 
	print(emp1.userDisplay)
	print(emp1.countDisplay)
except Exception as e:
	print (e)

