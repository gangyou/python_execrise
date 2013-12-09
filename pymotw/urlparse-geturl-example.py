from urlparse import urlparse
original = 'http://user:pass@NetLoc:80/path;parameters?query=argument#fragment'
print 'ORIG:', original
parsed = urlparse(original)
print 'PARSED:', parsed.geturl()
