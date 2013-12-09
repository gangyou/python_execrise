def checkio(data):

	initial_sofi, raise_sofi, initial_oldman, reduction_oldman = data
	current_sofi, current_oldman = initial_sofi, initial_oldman

	offered_sofi = False
	offered_oldman = True
	while current_sofi < current_oldman:
		if not offered_sofi:
			current_sofi += raise_sofi
			print "#Sofia: %d" % current_sofi
			offered_sofi = True
			offered_oldman = False

		if not offered_oldman:
			current_oldman -= reduction_oldman
			print "#Oldman: %d" % current_oldman
			offered_oldman = True
			offered_sofi = False



    #replace this for solution
	return current_sofi


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([150, 50, 1000, 100]) == 450, "1st example"
	assert checkio([150, 50, 900, 100]) == 400, "2nd example"
