import os

# where are we?
cwd = os.getcwd()
print "1", cwd

# go down
os.mkdir("samples")
print "2 mkdir"
os.chdir("samples")
print "3", os.getcwd()

# go back on
os.chdir(os.pardir)
print "4", os.getcwd()


