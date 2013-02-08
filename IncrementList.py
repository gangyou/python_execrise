class IncrementList(object):
	def __init__(self, start=0, step=1):
		self.start = start
		self.step = step
		self.changed = {}
	
	def __getitem__(self, index):
		if index in self.changed.keys():
			return self.changed[index]
		else:
			self.changed[index] = self.start + index * self.step
			return self.changed[index]

l = IncrementList(1,2)
print l[2]
print l[3]
