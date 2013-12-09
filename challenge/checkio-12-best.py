import types 
def checkio(arr):
	if type(arr) is types.ListType:
		return [x for i in arr for x in checkio(i)]
	else:
		return [arr]

if __name__ == '__main__':
    assert checkio([1,2,3]) == [1,2,3], 'First'
    assert checkio([1,[2,2,2],4]) == [1,2,2,2,4], 'Second'
    assert checkio([[[2]],[4,[5,6,[6],6,6,6],7]])\
                              == [2,4,5,6,6,6,6,6,7], 'Third'
    print('All ok')