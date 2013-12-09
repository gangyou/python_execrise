from itertools import ifilterfalse

def check_item(x):
	print 'Testing:', x
	return x < 1


for i in ifilterfalse(check_item, [-1,1,2,3,4,5, -2]):
	print i