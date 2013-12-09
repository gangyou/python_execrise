from UserList import UserList

class stack(UserList):
	def push(self, data):
		super(stack, self).append(data)

	def empty(self):
		return len(self.data) == 0

if __name__ == '__main__':
	s = stack()
	s.push(1)
	s.push(2)
	# print s.pop()
	assert s.pop() == 2, "should be 2"
	s.push(3)
	assert s.pop() == 3, 'should be 3'
	assert s.pop() == 1, 'should be 1'


	assert s.empty(), 'should be empty'