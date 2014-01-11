import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024)
		print '{} wrote:'.format(self.client_address[0])
		print self.data
		self.request.sendall(self.data.upper())

if __name__ == '__main__':
	server = SocketServer.TCPServer(('localhost', 8888), MyTCPHandler)

	server.serve_forever()