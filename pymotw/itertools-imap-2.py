from itertools import *

print 'Multiples:'
for i in imap(lambda x,y: (x, y, x*y), xrange(5), xrange(5,10)):
	print '%d * %d = %d' % i