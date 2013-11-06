import array

# unsigned char
a = array.array('B', range(16))
# signed short
b = array.array('h', range(16))

print a
print repr(a.tostring())

print b
print repr(b.tostring())