import fileinput, sys

for line in fileinput.input(inplace=1):
	if line[-2:] == '\r\n':
		line = line[:-2] + "\n"
	sys.stdout.write(line)