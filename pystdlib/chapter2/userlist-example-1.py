import UserList

class AutoList(UserList.UserList):

	def __init__(self):
		super(AutoList, self).__init__()

	def __setitem__(self, i, item):
		if i >= len(self.data):
			self.data.append(item)
		else:
			self.data[i] = item

list = AutoList()
for i in range(10):
	list.append(i)

print list