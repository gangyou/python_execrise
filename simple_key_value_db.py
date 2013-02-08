import shelve
class SimpleKeyValueDB(object):
	def __init__(self, filename):
		self.filename = filename
		self.db = shelve.open(filename, 'c')
		

	def __getitem__(self, index):
		try:
			return self.db[index]
		except:
			return None

	def __setitem__(self, index, value):
		try:
			self.db[index] = value
		except:
			print "save value for %s error" % index

	def close(self):
		try:
			self.db.close()
		except:
			print "Database closed!"


