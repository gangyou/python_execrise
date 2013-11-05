import UserString

class MyString(UserString.MutableString):
	def append(self, s):
		self.data = self.data + s

	def insert(self, index, s):
		self.data = self.data[index:] + s + self.data[index:]

	def remove(self, s):
		self.data = self.data.replace(s, "")

book = MyString("gannet and robin with nuthatch")

for bird in ['gannet', 'robin', 'nuthatch']:
	book.remove(bird)

print book