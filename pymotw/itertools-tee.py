from itertools import *

r = islice(count(), 5)
i1, i2 = tee(r)

for i in i1:
	print 'i1:', i

for i in i2:
	print 'i2:', i