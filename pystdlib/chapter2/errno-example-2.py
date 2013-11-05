import errno

try:
	fp = open("nosuchfile")
except IOError, (error, message):
	print error, repr(message)
	print errno.errorcode[error]
