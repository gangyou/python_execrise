def debug(f):
	msg = f.__name__
	def wrapper(*args, **kw):
		print msg
		return f(*args, **kw)

	return wrapper

@debug
def mul(x, y):
	print __name__
	return x*y

@debug
def div(x, y):
	print __name__
	return x*y

print mul(1,2)