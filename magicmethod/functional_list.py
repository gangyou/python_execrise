# coding=utf-8

class FunctionalList(object):
	def __init__(self, values=None):
		if values is None:
			self.values = []
		else:
			self.values = values

	def __len__(self):
		return len(self.values)

	def __getitem__(self, key):
		# may raise a KeyError if the key is not exists
		return self.values[key]

	def __setitem__(self, key, value):
		self.values[key] = value

	def __delitem__(self, key):
		del self.values[key]

	def __iter__(self):
		return iter(self.values)

	def __reversed__(self):
		return FunctionalList(reversed(self.values))

	def append(self, value):
		self.values.append(value)
		return self

	def head(self):
		return self.values[0]

	def tail(self):
		return self.values[1:]

	def init(self):
		return self.values[:-1]

	def last(self):
		return self.values[-1]

	def drop(self, n):
		return self.values[n:]

	def take(self, n):
		return self.values[:n]

if __name__ == '__main__':
	fl = FunctionalList()
	fl.append(1).append(2).append(3)
	for x in fl:
		print x

	print fl[2]
	print fl.take(2)

