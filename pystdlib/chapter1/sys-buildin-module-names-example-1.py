import sys

def dump(module):
	print module, "=>",
	if module in sys.builtin_module_names:
		print "<BUILDIN>"
	else:
		module = __import__(module)
		print module.__file__

dump("os")
dump("sys")
dump("string")
dump("strop")
dump("zlib")