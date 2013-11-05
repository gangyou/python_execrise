import tempfile, os

tempfile = tempfile.mkstemp()
print "tempfile", "=>", tempfile

file = open(tempfile, "w+b")
file.write("*" * 1000)
file.seek(0)
print len(file.read()), 'bytes'
file.close()

try:
	os.remove(tempfile[1])
except OSError:
	print "Remove error"