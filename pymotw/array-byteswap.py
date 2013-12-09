import array, binascii

def to_hex(a):
	chars_per_item = a.itemsize * 2
	hex_version = binascii.hexlify(a)
	num_chunks = len(hex_version) / chars_per_item
	for i in xrange(num_chunks):
		start = i * chars_per_item
		end = start + chars_per_item
		yield hex_version[start:end]

a1 = array.array('i', xrange(5))
a2 = array.array('i', xrange(5))