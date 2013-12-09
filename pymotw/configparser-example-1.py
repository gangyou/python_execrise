from ConfigParser import SafeConfigParser

filename = 'samples/sample.ini'

config = SafeConfigParser()
config.read(filename)


url = config.get('portal', 'url')
print url