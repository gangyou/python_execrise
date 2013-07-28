class Animal(object):
	def __init__(self, name, legs):
		self.name = name
		self.legs = legs
		self.stomach = []

	def __call__(self, food):
		self.stomach.append(food)

	def poop(self):
		if len(self.stomach) > 0:
			return self.stomach.pop(0)

	def __str__(self):
		return "A animal named %s" % (self.name)

if __name__ == '__main__':
	cow = Animal('king', 4)
	dog = Animal('floop', 4)
	print 'We have 2 animales a cow name \
	%s and dog named %s, both have %s legs' \
	% (cow.name, dog.name, cow.legs)
	print cow # here __str__ method work

	# We give food to cow
	cow('grass')
	print cow.stomach

	# We feed dog
	dog('bone')
	dog('beef')
	print dog.stomach
