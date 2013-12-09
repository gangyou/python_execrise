FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
	if number < 20:
		result = (FIRST_TEN + SECOND_TEN)[number]
	elif number < 100:
		result = (['','',] + OTHER_TENS)[number // 10]
		if number % 10:
			result += ' ' + checkio(number % 10)
	elif number < 1000:
		result = checkio(number // 100) + ' hundred'
		if number % 100:
			result += ' ' + checkio(number % 100)
	return result

if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"