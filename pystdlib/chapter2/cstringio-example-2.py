# backwards to StringIO when cStringIO is missing

try:
	import cStringIO
	StringIO = cStringIO
except ImportError:
	import StringIO

print StringIO