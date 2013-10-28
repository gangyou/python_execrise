import sys

print sys.platform

if sys.platform == 'win32':
	import ntpath
	pathmodule = ntpath
elif sys.platform == 'darwin':
	import macpath
	pathmodule = macpath
else:
	import posixpath
	pathmodule = posixpath

print pathmodule