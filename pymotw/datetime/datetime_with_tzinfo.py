from datetime import tzinfo, datetime, timedelta

class GMT8(tzinfo):
	def utcoffset(self, dt):
		return timedelta(hours=8) + self.dst(dt)

	def dst(self, dt):
    	pass