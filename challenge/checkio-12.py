import types
def checkio(data):
	result = []
	flat(data, result)
	return result

def flat(l, flat_list=[]):
	for elem in l:
		if type(elem) is types.ListType:
			flat(elem, flat_list)
		else:
			flat_list.append(elem)

if __name__ == '__main__':
    assert checkio([1, 2, 3]) == [1, 2, 3], 'First example'
    assert checkio([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], 'Second example'
    assert checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) ==\
        [2, 4, 5, 6, 6, 6, 6, 6, 7], 'Third example'