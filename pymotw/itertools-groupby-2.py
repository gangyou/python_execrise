from itertools import *

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Point(%s, %s)' % (self.x, self.y)

	def __cmp__(self, other):
		return cmp((self.x, self.y), (other.x, other.y))

# Create a dataset of Point instances
data = list(imap(Point, cycle(islice(count(), 3)), islice(count(), 10),))
print 'Data:', data
print 

# Try to group the unsorted data based on X values
print 'Grouped, unsorted:'
for k, g in groupby(data, lambda o: o.x):
	print k, list(g)
print 

# Sort the data
data.sort()
print 'Sorted:', data
print 

# Group the sorted data based on X values
print 'Grouped, sorted'
for k, g in groupby(data, lambda o: o.x):
	print k, list(g)
print