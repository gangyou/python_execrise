import urllib, re

uri = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
nothing = "8022"
pattern = re.compile(r'and the next nothing is (\d+)')

while True:
	try:
		res = urllib.urlopen(uri % nothing)
		nothing = re.search(pattern, res.read()).group(1)
		print nothing
	except:
		break

print nothing
