import re
# * + , {} => symbols used

def all_matches(text, pattern):
	print(pattern)
	regobj = re.compile(pattern)
	for m in regobj.finditer(text):
		print('Start : {0}, End: {1}, Word: {2}'.format(m.start(), m.end(), text[m.start(): m.end()]))

# greedy parsing 
all_matches('Searching for pattern in text', 'pattern')
all_matches('xyyxxxxyyyyxxxxyy', 'xy*') #x folowed by more y or none
all_matches('xyyxxxxyyyyxxxxyy', 'xy+') # x followed by more than y
all_matches('xyyxxxxyyyyxxxxyy', 'xy?') # x folowed by one or zero y
all_matches('xyyxxxxyyyyxxxxyy', 'xy{2,3}') # x followed by 2-3 y
all_matches('xyyxxxxyyyyxxxxyy', 'xy{2,}') # x followed by 2 or more y

all_matches('xyyxxxxyyyyxxxxyy', 'x[xy]+') # x followed by x or y
all_matches('xx..  ..yyyxxx.. ', '[^. ]+') # all string with no . and space
all_matches('A94B2c4 xyz08', '[A-Z][0-9]') # all maj followed by digits
all_matches('A94B2c4 xyz08', '[A-Za-z][0-9]')

# r = to use \
all_matches('Batna roads', r'B\w+a') # starts with B and ends with a without spaces


"""
\d : digits \D : except digits
\s : white spaces \S excepts spaces
\w : alphaNum \W excepts alphaNum
"""
# r :  to use \
all_matches('This is 1-st example', r"\d+") # numbers
all_matches('This is 1-st example', r"\D+") # but num
all_matches('This is 1-st example', r"\S+") # no spaces

"""
$ end of string
^ beginning of string
\A the word of the beginning of string
\Z the word at the end of the string
"""
all_matches('Relative positioning in regular expression', r'^\w+') # first word
all_matches('Relative positioning in regular expression', r'\w+$') # last word


# non greedy
all_matches('xyyxxxxyyyyxxxxyy', 'xy*?') # find only x followed by y or none
all_matches('xyyxxxxyyyyxxxxyy', 'xy+?') #
all_matches('xyyxxxxyyyyxxxxyy', 'xy{2,}?')