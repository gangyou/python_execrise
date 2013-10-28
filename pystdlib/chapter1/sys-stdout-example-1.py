import sys, string

class Redirect(object):
	def __init__(self, stdout):
		self.stdout = stdout

	def write(self, s):
		self.stdout.write(string.lower(s))

old_stdout = sys.stdout
sys.stdout = Redirect(sys.stdout)

print "HEJA SVERIGE"
print "FRISKT HUM\303\226R"

sys.stdout = old_stdout

print "M\303\205\303\205\303\205\303\205L!"