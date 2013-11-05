import zlib

encoder = zlib.compressobj()

data = encoder.compress("life")
data += encoder.compress(" of ")
data += encoder.compress("brian")
data += encoder.flush()

print repr(data)
print repr(zlib.decompress(data))