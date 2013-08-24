import os

os.makedirs("test/multiple/levels")

fp = open("test/multiple/levels/file", "w")
fp.write("inspector praline")
fp.close()

# first remove the file
os.remove("test/multiple/levels/file")

# remove the dir
os.removedirs("test/multiple/levels")