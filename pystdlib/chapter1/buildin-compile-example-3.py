import sys, string

class CodeGeneratorBackend(object):
	"Simple code generator for python"

	def begin(self, tab="\t"):
		self.code = [];
		self.tab = tab;
		self.level = 0;

	def end(self):
		self.code.append("")
		return compile(string.join(self.code, "\n"), "<code>", "exec")

	def write(self, code):
		self.code.append(self.tab * self.level + code)

	def indent(self):
		self.level += 1

	def dedent(self):
		self.level -= max(0, self.level - 1)

c = CodeGeneratorBackend()
c.begin()
c.write("for i in range(5):")
c.indent()
c.write("print 'code generaton made easy!'")
c.dedent()
exec c.end()


