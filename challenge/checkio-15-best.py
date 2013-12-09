def checkio(data):
	a,b = data
	return str(bin(a^b)).count(1)