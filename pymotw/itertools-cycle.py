from itertools import *

i = 0
for item in cycle(['a', 'b', 'c']):
	i += 1
	if i == 10: break
	print (i, item)