import sys

print "hello"

try:
	sys.exit(1)
except SystemExit:
	print "exception in try catch"

# will be print
print "there"