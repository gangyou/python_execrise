class C(object):
	def __init__(self):
		self._x = None

	def getx(self):
		return self._x

	def setx(self, value):
		self._x = value

	def delx(self):
		del self._x

	x = property(getx, setx, delx, "I'm the x property")

class Parrot(object):
	def __init__(self):
		self._voltage = 100000

	@property
	def voltage(self):
		""" Get the current voltage. """
		return self._voltage

class C1(object):
	def __init__(self):
		self._x = None

	@property
	def x(self):
		""" I'm the 'x' property """
		return self._x

	@x.setter
	def x(self, value):
		self._x = value

	@x.deleter
	def x(self):
		del self._x

if __name__ == '__main__':
	c = C()
	print c.x # None
	c.x = 2
	print c.x # 2

	p = Parrot()
	print p.voltage # 100000
	p.voltage = 100 # Opps! Can't set attribute