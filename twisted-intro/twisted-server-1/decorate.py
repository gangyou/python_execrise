import functools

class function_wrapper(object):
	def __init__(self, wrapped):
		self.wrapped = wrapped
		functools.update_wrapper(self, wrapped)

	def __call__(self, *args, **kwargs):
		print 'Wrapped function'
		return self.wrapped(*args, **kwargs)

class Class(object):
	@function_wrapper
	@classmethod
	def cmethod(cls):
		pass
