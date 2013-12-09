import locale, os, pprint

print 'Environment settings'
for env_name in ['LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE']:
	print '\t%s = %s' % (env_name, os.environ.get(env_name, ''))

# What is the default locale
print 
print 'Default locale:', locale.getdefaultlocale()

# Default settings based on the user's environment
locale.setlocale(locale.LC_ALL, '')

# If we do not have a locale, assume US English
print 'From environment:', locale.getlocale()

pprint.pprint(locale.localeconv())