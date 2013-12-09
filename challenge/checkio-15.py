def checkio(data):
    a, b = data
    return sum([1 for x,y in zip("{:016b}".format(a), "{:016b}".format(b)) if x != y])

if __name__ == '__main__':

	assert checkio([117, 17]) == 3, "First example"
	assert checkio([1, 2]) == 2, "Second example"
	assert checkio([16, 15]) == 5, "Third example"