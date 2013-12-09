from itertools import *

for i in repeat('over-and-over', 5):
	print i

for no, s in izip(count(), repeat('over-and-over', 5)):
	print no, s