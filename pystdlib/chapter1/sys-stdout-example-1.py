import sys, string

class Redirect(object):
	def __init__(self, stdout):
		self.stdout = stdout

	def write(self, s):
		self.stdout.write(string.lower(s))

old_stdout = sys.stdout
sys.stdout = Redirect(sys.stdout)

print "HEJA SVERIGE"

sys.stdout = old_stdout