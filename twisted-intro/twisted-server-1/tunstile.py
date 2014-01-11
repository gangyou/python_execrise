class Turnstile(object):
	def __init__(self):
		self.locked = True

	# Two methods to react to real-world events
	def toke_inserted(self):
		self.unlock()

	def arm_rotated(self):
		self.lock()

	# Two methods to effect change in the real-world
	def lock(self):
		if self.locked:
			return

		self.locked = True

	def unlock(self):
		if not self.locked:
			return

		self.locked = False

