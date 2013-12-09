from urlparse import urldefrag
original = 'http://user:pass@NetLoc:80/path;parameters?query=argument#fragment'
print original
url, fragment = urldefrag(original)
print url
print fragment