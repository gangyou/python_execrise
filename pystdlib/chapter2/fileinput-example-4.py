import fileinput

# iterate over the lines of all files listed in sys.argv[1:]
for line in fileinput.input():
	print line