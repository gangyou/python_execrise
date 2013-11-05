import fnmatch, os

for file in os.listdir("samples"):
	if fnmatch.fnmatch(file, "*.txt"):
		print file

