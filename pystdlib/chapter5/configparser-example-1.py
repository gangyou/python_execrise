import ConfigParser

config = ConfigParser.ConfigParser()
config.read("sample.cfg")

# print summary
print
print config.get('book', 'title')
print 'by', config.get('book', 'author')
print "(", config.get('book', 'email'), ")"
print
print config.get('ematter', 'pages'), 'pages'
print

# dump entire config file
for section in config.sections():
	print section
	for option in config.options(section):
		print " ", option, '=', config.get(section, option)