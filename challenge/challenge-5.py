import pickle, urllib

uri = 'http://www.pythonchallenge.com/pc/def/banner.p'

try:
	source = urllib.urlopen(uri)
	result = pickle.load(source)
	source.close()

	for elt in result:
		print ''.join([e[1] * e[0]  for e in elt ])
except:
	print 'error'
