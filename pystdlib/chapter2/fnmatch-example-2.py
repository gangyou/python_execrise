import fnmatch, os, re

pattern = fnmatch.translate("*.txt")

for file in os.listdir("samples"):
	if re.match(pattern, file):
		print file

print "(pattern was %s)" % pattern