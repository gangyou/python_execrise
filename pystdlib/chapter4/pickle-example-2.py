import pickle, math

value = (
	"this is a long string",
	[1.2345678, 2.345678, 3.456789] * 100
	)

# text mode
data = pickle.dumps(value)
print type(data), len(data), pickle.loads(data) == value

# binary mode
data = pickle.dumps(value, 1)
print type(data), len(data), pickle.loads(data) == value 