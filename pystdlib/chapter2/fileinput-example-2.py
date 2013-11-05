import fileinput
import glob, string, sys

for line in fileinput.input(glob.glob("samples/*.txt")):
	if fileinput.isfirstline():
		sys.stderr.write("-- reading %s --\n" % fileinput.filename())
	sys.stdout.write(str(fileinput.lineno()) + " " + string.upper(line))