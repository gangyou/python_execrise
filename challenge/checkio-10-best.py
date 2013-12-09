import string
TO_MORSE = string.maketrans('01', '.-')

def to_morse(number, bits):
	return "{0:0{1}b}".format(number, bits).translate(TO_MORSE)

def to_code(field):
	tens, ones = divmod(int(field), 10)
	return "{} {}".format(to_morse(tens, 3), to_morse(ones, 4))

def checkio(data):
	return " : ".join(map(to_code, data.split(':')))[1:]
