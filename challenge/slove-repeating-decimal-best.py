def checkio(fraction):
	numerator, denominator = fraction
	integer, remainer = divmod(numerator, denominator)

	mod_accumulator = []

	def recurse_divmod(mod, denominator, historical_dividend=[]):
		global rstart
		if mod == 0:
			return []

		if mod in historical_dividend:
			historical_dividend.append(mod)
			return []

		historical_dividend.append(mod)
		results = []
		div, mod = divmod(mod * 10, denominator)
		results += [div] + recurse_divmod(mod, denominator, historical_dividend)
		return results

	decimal_parts = recurse_divmod(remainer, denominator, mod_accumulator)
	
	rstart = 0
	
	return "{}.{}({})".format( integer,
		"".join([str(x) for x in decimal_parts[:rstart]]),
		"".join([str(x) for x in decimal_parts[rstart:]])
		)

	

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([1, 3]) == "0.(3)", "1/3 Classic"
	assert checkio([5, 3]) == "1.(6)", "5/3 The same, but bigger"
	print checkio([29, 12])
	assert checkio([29, 12]) == "2.41(6)", "29/12 not and repeating part"
	assert checkio([3, 8]) == "0.375", "3/8 without repeating part"
	assert checkio([7, 11]) == "0.(63)", "7/11 prime/prime"
	assert checkio([11, 7]) == "1.(571428)", "11/7 six digits"
	assert checkio([2, 21]) == "0.(095238)", "2/21 six digits"