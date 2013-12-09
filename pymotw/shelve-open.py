import shelve

s = shelve.open('test_shelf.db')
try:
	existing = s['key1']
finally:
	s.close()

print existing