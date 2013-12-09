
import string
def normalize(data):
	return ("{:02}"*3).format(*[int(x) for x in data.split(':')])

def to_binary(data):
	return "{:02b} {:04b} : {:03b} {:04b} : {:03b} {:04b}".format(*[int(x) for x in data])

def to_morse(data):
	table = string.maketrans('01', '.-')
	return string.translate(data, table)

def checkio(data):
	data = normalize(data)
	binary = to_binary(data)
	return to_morse(binary)

if __name__ == '__main__':
	assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
	assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
	assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"