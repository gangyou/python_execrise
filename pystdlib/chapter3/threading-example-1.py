import threading, time, random

class Counter(object):
	def __init__(self):
		self.lock = threading.Lock()
		self.value = 0

	def increment(self):
		self.lock.acquire() # critical section
		self.value = value = self.value + 1
		self.lock.release()
		return value

counter = Counter()

class Worker(threading.Thread):
	def run(self):
		for i in range(10):
			# pretend we're doing something that takes 10000ms
			value = counter.increment() # increment global counter
			time.sleep(random.randint(10, 100) / 1000.0)
			print self.getName(), " -- task", i, "finished", value

for i in range(10):
	Worker().start()			
