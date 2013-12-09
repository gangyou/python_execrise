from itertools import starmap

for item in starmap(lambda x,y: (x, y, x*y), [(x,y) for x in range(5) for y in range(5,10)] ):
	print '%d * %d = %d' % item