from urlparse import urlparse, urlunparse
original = 'http://user:pass@NetLoc:80/path;parameters?query=argument#fragment'
parsed = urlparse(original)
print 'Parsed:',  parsed

t = parsed[:]
print 'TUPLE:', urlunparse(t)
