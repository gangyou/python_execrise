import time

class Slate(object):

	'''Class to store a string and a changelog, and forget its value when pickle.'''

	def __init__(self, value):
		self.value = value
		self.last_change = time.asctime()
		self.history = {}

	def change(self, new_value):
		# Change the value. Commit last value to history
		self.history[self.last_change] = self.value
		self.value = new_value
		self.last_change = time.asctime()

	def __getstat__(self):
		# Deliberately do not return self.value or self.last_change.
		# We want to have a "blank slate" when we unpickle.
		return self.history

	def __setstate__(self, state):
		# Make self.history = state and last_change and value undefined
		self.history = state
		self.value, self.last_change = None, None

	def __repr__(self):
		return """
			history: %s,
			last_change: %s
			""" % (self.history, self.last_change)

if __name__ == '__main__':
	slate = Slate("A Slate form Saint")
	import pickle
	slate.change("Line 1")
	slate.change("line 2")

	jar = open('slate.pkl', 'wb')
	pickle.dump(slate, jar)
	jar.close()

	pkl_file = open('slate.pkl', 'rb')
	data = pickle.load(pkl_file)
	print data
	pkl_file.close()