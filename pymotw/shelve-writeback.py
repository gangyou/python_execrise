import shelve

s = shelve.open('test_shelf.db', writeback=True)
try:
	print s['key1']
	s['key1']['new_value'] = 'this was not here before'
	print s['key1']
finally:
	s.close()

s = shelve.open('test_shelf.db', writeback=True)
try:
	print s['key1']
finally:
	s.close()