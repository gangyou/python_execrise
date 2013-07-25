def printdebug_level(level):
	def printdebug(func):
		def __decorator(user):
			print 'enter the login, and debug level %d' % level
			func(user)
			print 'exit the login'
		return __decorator
	return printdebug

@printdebug_level(level=5)
def login(user):
	print 'in login %s' % user

login('eric')