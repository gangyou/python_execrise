class movement(object):
	def __init__(self, x_delta, y_delta, direct):
		self._x_delta = x_delta
		self._y_delta = y_delta
		self._direct = direct

	@property
	def deltaX(self):
		return self._x_delta

	@property
	def deltaY(self):
		return self._y_delta

	@property
	def toDirect(self):
		return self._direct