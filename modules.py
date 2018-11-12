# Reuse code from other files 
# if file is in same file
# import filename 
# import filename as name
# from filename import function
# dir(filename) return all functions with in the file  

import sys 
sys.path.append('./modules') # if module is not in same directory
import prime
print (prime.PrimesTo(5))
print(dir(prime))