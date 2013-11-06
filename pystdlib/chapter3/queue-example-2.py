import threading, Queue, time, random

WORKERS = 2

class Worker(threading.Thread):
	def __init__(self, queue):
		self._queue = queue
		super(Worker, self).__init__()

	def run(self):
		while 1:
			item = self._queue.get()
			if item is None:
				break

			# pretend we're doing somethin that takes time
			time.sleep(random.randint(10, 100) / 1000.0)

			print "task", item, "finished"


# run with limited queue

queue = Queue.Queue(3)

for i in range(WORKERS):
	Worker(queue).start()

for item in range(10):
	print "push", item
	queue.put(item)

for i in range(WORKERS):
	queue.put(None)