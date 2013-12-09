from itertools import ifilter

def check_item(x):
	print 'Testing:', x
	return x < 1

for i in ifilter(check_item, [-1, 0, 1, 2,3,4]):
	print i