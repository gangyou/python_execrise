# coding:utf-8

def checkio(data):
	count = 0
	sticks = combinations(data)
	for stick in sticks:
		longest = max(stick)
		stick.remove(longest)
		if sum(stick) < longest:
			count += 1

	return count

def combinations(data):
	sticks = []
	n = len(data)
	for i in range(1, 1 << n):
		if one_appear_times(i) == 3:
			sticks.append(bitmap_list(data, i))
	return sticks

def one_appear_times(number):
	return "{:b}".format(number).count("1")

def bitmap_list(data, number):
	result = []
	for i in range(len(data)):
		if number & (1 << i):
			result.append(data[i])
	return result

if __name__ == '__main__':
	assert bitmap_list([1,2,3,4,5], 5) == [1,3], "bitmap 101, 应该返回[1,3]"
	assert bitmap_list([1,2,3,4,5], 0) == [], "bitmap 0, 啥都不返回"
	assert bitmap_list([1,2,3,4,5], 1) == [1], "bitmap 1, 返回[1]"
	assert bitmap_list([1,2,3,4,5], 31) == [1,2,3,4,5], "bitmap 1, 全部返回来"
	assert checkio((4, 2, 10)) == 1, "First"
	assert checkio((1, 2, 3)) == 0, "Second"
	assert checkio((5, 2, 9, 6)) == 2, "Third"