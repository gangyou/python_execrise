FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

def below_ten(number):
  if not 0 <= number < 10: raise Exception
  return FIRST_TEN[number]

def ten_to_nintynine(number):
  if not 10 <= number < 100: raise Exception
  if 10 <= number < 20: 
    return SECOND_TEN[number % 10]
  elif number % 10 == 0:
    return OTHER_TENS[number // 10 - 2]
  else:
    return "{} {}".format(OTHER_TENS[ number // 10 - 2 ], below_ten(number % 10))

def more_than_hundred(number):
  if not 100 <= number < 1000: raise Exception
  if number % 100 == 0: return "{} {}".format(below_ten(number // 100), HUNDRED)
  elif number % 100 > 10:
    return "{} {} {}".format(below_ten(number // 100), HUNDRED, ten_to_nintynine(number % 100))
  else:
    return "{} {} {}".format(below_ten(number // 100), HUNDRED, below_ten(number % 100))


def checkio(number):
    if len(str(number)) == 1:  return below_ten(number)
    elif len(str(number)) == 2:  return ten_to_nintynine(number)
    else: return more_than_hundred(number)
    #replace this for solution
    # return 'string representation of n'

#Some hints
#Don't forget strip whitespaces at the end of string


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
