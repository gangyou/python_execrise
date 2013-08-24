import os

def callback(arg, directory, files):
	for file in files:
		fullpath = os.path.join(directory, file)
		print fullpath, "size: ", os.stat(fullpath)[6]

os.path.walk(".", callback, "secret message")