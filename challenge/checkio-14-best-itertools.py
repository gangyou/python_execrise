import itertools
def checkio(values):
	return sum(1 for c in itertools.combinations(sorted(values), 3) if c[2]>(c[0] + c[1]))

if __name__ == '__main__':
	assert checkio((4, 2, 10)) == 1, "First"
	assert checkio((1, 2, 3)) == 0, "Second"
	assert checkio((5, 2, 9, 6)) == 2, "Third"