import SocketServer

class MyTCPHandler(SocketServer.StreamRequestHandler):
	def handle(self):
		self.data = self.rfile.readline().strip()
		print '{} wrote:'.format(self.client_address[0])
		print self.data
		self.wfile.write(self.data.upper())

if __name__ == '__main__':
	server = SocketServer.TCPServer(('localhost', 8888), MyTCPHandler)

	server.serve_forever()