def checkio(fraction):
	numerator, denominator = fraction

	integer, remainer = divmod(numerator, denominator)

	decimal_part = []
	historical_dividend = []
	repeating_starts_index = -1

	while True:
		if remainer < denominator:
			remainer, results = scale(remainer, denominator)
			decimal_part += results

		if remainer in historical_dividend:
			repeating_starts_index = historical_dividend.index(remainer)
			break

		historical_dividend.append(remainer)
		quotial, remainer = divmod(remainer, denominator)
		decimal_part.append(quotial)

		if not remainer:
			break
    
	if not decimal_part[-1]:
		decimal_part = decimal_part[:-1]

	if repeating_starts_index >= 0:
		decimal_norepeat = "".join([str(x) for x in decimal_part[:repeating_starts_index]])
		decimal_repeat = "".join([str(x) for x in decimal_part[repeating_starts_index:]])
		return "{}.{}({})".format(integer, decimal_norepeat, decimal_repeat)
	else:
		return "{}.{}".format(integer, "".join([str(x) for x in decimal_part]))


def scale(remainer, divisor):
    results = []
    if remainer < divisor:
        remainer *= 10

    if remainer >= divisor:
        return (remainer, results)

    while remainer < divisor:
        results += [0]
        remainer *= 10

    return (remainer, results)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([1, 3]) == "0.(3)", "1/3 Classic"
	assert checkio([5, 3]) == "1.(6)", "5/3 The same, but bigger"
	assert checkio([3, 8]) == "0.375", "3/8 without repeating part"
	assert checkio([7, 11]) == "0.(63)", "7/11 prime/prime"
	assert checkio([29, 12]) == "2.41(6)", "29/12 not and repeating part"
	assert checkio([11, 7]) == "1.(571428)", "11/7 six digits"
	assert checkio([2, 21]) == "0.(095238)", "2/21 six digits"