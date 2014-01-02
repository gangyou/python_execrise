import threading
import SocketServer

class ThreadedEchoRequestHandler(SocketServer.BaseRequestHandler):
	# Echo the back to the client
	def handle(self):
		data = self.request.recv(1024)
		cur_thread = threading.currentThread()
		response = '%s: %s' % (cur_thread.getName(), data)
		self.request.send(response)
		return

class ThreadedEchoServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):pass

if __name__ == '__main__':
	import socket
	import threading

	address = ('localhost', 0)
	server = ThreadedEchoServer(address, ThreadedEchoRequestHandler)
	ip, port = server.server_address

	t = threading.Thread(target=server.serve_forever)
	t.setDaemon(True)
	t.start()
	print 'Server loop running in thread:', t.getName()

	# Connect to the server
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))

	# Send the data
	message = 'Hello World'
	print 'Sending: %s ' % message
	len_sent = s.send(message)

	# Receive a response
	response = s.recv(1024)
	print 'Received: %s' % response

	# Clean up
	s.close()
	
	server.socket.close()