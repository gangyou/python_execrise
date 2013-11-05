dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}

viewkeys = dishes.viewkeys()
viewvalues = dishes.viewvalues()
keys = dishes.keys()
values = dishes.values()

# iteration
n = 0
for value in viewvalues:
	n += value
print n # 504

print 'keys in view', list(viewkeys)
print 'keys', list(keys)
# ['eggs', 'bacon', 'sausage', 'spam']
print 'values in view', list(viewvalues)
print 'values', list(values)
# [2, 1, 1, 500]

del dishes['eggs']
del dishes['sausage']

print 'after deletion'
print 'keys in view', list(viewkeys)
print 'keys', list(keys)
print 'values in view', list(viewvalues)
print 'values', list(values)

