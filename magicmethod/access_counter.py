# coding=utf-8

class AccessCounter(object):
	'''一个能够记录访问次数的类'''

	def __init__(self, val):
		super(AccessCounter, self).__setattr__('counter', 0)
		super(AccessCounter, self).__setattr__('value', val)

	def __setattr__(self, name, value):
		if name == 'value':
			super(AccessCounter, self).__setattr__('counter', self.counter + 1)

		super(AccessCounter, self).__setattr__(name, value)

	def __delattr__(self, name):
		if name == 'value':
			super(AccessCounter, self).__setattr__('counter', self.counter + 1)
		super(AccessCounter, self).__delattr__(name)

	def count(self):
		return super(AccessCounter, self).__getattribute__('counter')

if __name__ == '__main__':
	counter = AccessCounter(2)
	counter.value = 1
	counter.value = 2
	print counter.count()
	del counter.value
	print counter.count()