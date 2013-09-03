import sys

print "path has", len(sys.path), "members"
for path in sys.path:
	print path

# oops!
sys.path = []
import random