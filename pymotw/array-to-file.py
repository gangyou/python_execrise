import array
import binascii
import tempfile

a = array.array('i', xrange(5))
print 'A1:', a

# Write the array of numbers to the file
# From PyDoc: The returned object is always a file-like object whose file attribute is the underlying true file object. 
output = tempfile.NamedTemporaryFile()
# Must be the *acutual* file
a.tofile(output.file)
output.flush()

# Read the raw data
input = open(output.name, 'rb')
raw_data = input.read()
print 'Raw Contents:', binascii.hexlify(raw_data)

# Read the data into an array
input.seek(0)
a2 = array.array('i')
a2.fromfile(input, len(a))
print 'A2:', a2