from itertools import repeat, imap, count

for i in imap(lambda x, y: (x, y, x*y), repeat(2, 5), count()):
	print '%d * %d = %d' % i