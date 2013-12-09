#coding:utf8
# Path 表达式 (定点序号， 路径， 最小值)
class Point(object):
	def __init__(self, name, path='', weight=999):
		self.name, self.path, self.weight = name, path, weight

	def getname(self):
		return self.name

	def getpath(self):
		return self.path

	def getweight(self):
		return self.weight

	def updateweight(self, value):
		self.weight = value

	def updatepath(self, path):
		self.path = path

	def __repr__(self):
		return "<{}, path : {}, weight: {}>".format(self.name, self.path, self.weight)

	def __str__(self):
		return self.__repr__()

class Graph(object):
	def __init__(self, data):
		self.data = data
		self.dimension = len(data)

	def _getxy(self, point, other_point):
		x = max(0, point.getname() - 1 )
		y = max(0, other_point.getname() - 1 )
		return (x, y)

	def isconnected(self, point, other_point):
		x, y = self._getxy(point, other_point)
		if self.data[x][y]:
			return True
		return False

	def weight(self, point, other_point):
		x, y = self._getxy(point, other_point)
		if self.isconnected(point, other_point):
			return self.data[x][y]
		return 999

def dijkstra(data):
	U, S, graph = [], [], Graph(data)
	for i in range(1, len(data) + 1):
		U.append(Point(i))

	V = U.pop(0)
	S.append(V)
	V.updateweight(0)
	# 当前考察的路径
	P = str(V.getname())
	while U:
		#以当前点为中心点，更新U中所有的值
		for point in U:
			weight = graph.weight(V, point) + V.weight
			if weight and weight < point.getweight():
				point.updatepath(P + str(point.getname()))
				point.updateweight(weight)

		# 选出U中最小的点，添加到S
		V = min(U, key=lambda x : x.getweight())
		P = V.getpath()
		S.append(V); U.remove(V)


	return S.pop().getweight()



if __name__ == '__main__':
	data = [
		[0, 6, 3, 0, 0, 0],
		[6, 0, 2, 5, 0, 0],
		[3, 2, 0, 3, 4, 0],
		[0, 5, 3, 0, 2, 3],
		[0, 0, 4, 2, 0, 5],
		[0, 0, 0, 3, 5, 0],
	]
	graph = Graph(data)
	point = Point(1)
	other_point = Point(2)
	assert graph.isconnected(point, other_point), "A点和B点之间是相连的"
	assert graph.weight(point, other_point) == 6, "A和B直接的距离是6"
	assert dijkstra(data) == 9, "最短路径应该是9"