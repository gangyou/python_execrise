class Closer:
	'''A context manager to automatically close an object with a close method in a with statement.'''

	def __init__(self, obj):
		self.obj = obj

	def __enter__(self):
		return self.obj

	def __exit__(self, exception_type, exception_val, trace):
		try:
			self.obj.close()
		except AttributeError:
			print 'Not closable.'
			return True

if __name__ == '__main__':
	from fptlib import FTP
	with Closer(FTP('ftp.somesite.com')) as conn:
		conn.dir()

	conn.dir()

	with Close(int(5)) as i:
		i += 1

