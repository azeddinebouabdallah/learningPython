# automats = regular languages
import re

print(re.search('none', 'Seaching pattern in text')) # Search on given text 
match = re.search('pattern', 'Seaching pattern in text')
print(match)

# Important methods and attributes
print(match.re.pattern) # the result 
print(match.string) # the given text
print(match.start()) # 1st index of the result
print(match.end()) # Ending index

### use obj that holds regex
regex = re.compile('pattern') # regex object with pattern
# Now we can search calling only regex

print(regex.search('Seaching pattern in text'))

# If the result has double results
print(regex.search('Seaching pattern in text pattern'))# Finds the 1st one
# Instead
print("###")
print(regex.findall('Seaching pattern in text pattern')) # list of all result

# match function (the beginning)
print(re.match('Match', 'Match function test'))
print(re.match('test', 'Match function test')) # None






