import Queue

Empty = Queue.Empty

class Stack(Queue.Queue):

	def __init__(self):
		# Queue is old class
		Queue.Queue.__init__(self, 0)

	def _put(self, item):
		# insert at the beginning of queue, not at the end
		self.queue.insert(0, item)

	# method alias
	push = Queue.Queue.put
	pop = Queue.Queue.get
	pop_nowait = Queue.Queue.get_nowait

# try it 
stack = Stack()

# push items on stack
stack.push("first")
stack.push("second")
stack.push("third")

first_out = stack.pop_nowait()
assert first_out == 'third'
