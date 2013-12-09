'''
An integer is said to be a palindrome if it is equal to its reverse in a string form. For example, 79197 and 324423 are palindromes. In this task you will be given an integer N. You must find the smallest integer M >= N such that M is a prime number and also a palindrome. 
Input: N. An integer.
Output: A prime palindrome. An integer.
Example:
'''
import math

def checkio(number):
	while True :
		if all([is_prime(number), is_palindrome(number)]):
			return number
		number += 1

	return number

def is_prime(number):
	if not number > 0: return False
	limit = int(math.sqrt(number))
	for i in range(2, limit + 1):
		if number % i == 0: return False
	return True

def is_palindrome(number):
	number_str = str(number)
	if number_str == number_str[::-1]:
		return True
	return False

if __name__ == '__main__':
	assert checkio(31) == 101, 'First example'
	assert checkio(130) == 131, 'Second example'
	assert checkio(131) == 131, 'Third example'
	print is_prime(121)