# I 1 (unus)
# V 5 (quinque)
# X 10 (decem)
# L 50 (quinquaginta)
# C 100 (centum)
# D 500 (quingenti)
# M 1,000 (mille)
UNIT_SYNTAX = ('I', 'V', 'X')
DECADE_SYNTAX = ('X', 'L', 'C')
THOUND_SYNTAX = ('C', 'D', 'M')
ONE_THOUND = 'M'

def trans(digit, syntax):
	if digit == 0: return ''

	if digit == 5: 
		return syntax[1]
	elif digit < 5:
		if digit == 4:
			return syntax[0] + syntax[1]
		else:
			return digit * syntax[0]
	else:
		if digit == 9:
			return syntax[0] + syntax[2]
		else:
			return syntax[1] + (digit - 5) * syntax[0] 

def checkio(data):
	unit = data % 10;
	decade = (data % 100) // 10
	thound = (data % 1000) // 100
	d_thound = (data // 1000)
	return d_thound * ONE_THOUND + trans(thound, THOUND_SYNTAX) + trans(decade, DECADE_SYNTAX) + trans(unit, UNIT_SYNTAX)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(6) == 'VI', '6'
	assert checkio(76) == 'LXXVI', '76'
	assert checkio(499) == 'CDXCIX', '499'
	assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'