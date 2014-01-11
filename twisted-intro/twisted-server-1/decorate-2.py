from functools import function_wrapper

class Class(object):
	@function_wrapper
	@classmethod
	def cmethod(cls):
		pass