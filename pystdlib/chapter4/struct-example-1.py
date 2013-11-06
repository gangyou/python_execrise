import struct

# native byteorder
buffer = struct.pack("ihb", 1,2,3)
print repr(buffer)
print struct.unpack("ihb", buffer)

# data from a sequence, network byteorder
data = range(1, 4)
buffer = apply(struct.pack, ("!ihb",) + tuple(data))
print repr(buffer)
print struct.unpack("!ihb", buffer)