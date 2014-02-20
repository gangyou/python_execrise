from decimal import Decimal

class Fees(object):

	def __init__(self):
		self._fee = None

	@property
	def fee(self):
		return self._fee

	@fee.setter
	def fee(self, value):
		if isinstance(value, str):
			self._fee = Decimal(value)     
		elif isinstance(value, Decimal):
			self._fee = value

