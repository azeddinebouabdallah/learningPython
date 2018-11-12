import pdb

print('Statement 1')
for i in range(10):
	print('Statement', str(i+1))
pdb.set_trace() 

print("statement7")
pdb.pm() # If there's an error it would debug