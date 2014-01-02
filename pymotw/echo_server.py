import logging
import sys
import SocketServer

logging.basicConfig(level=logging.DEBUG,
	format='%(name)s: %(message)s',)

class EchoRequestHandler(SocketServer.BaseRequestHandler):
	
	def __init__(self, request, client_address, server):
		self.logger = logging.getLogger('EchoRequestHandler')
		self.logger.debug('__init__')
		super(SocketServer.BaseRequestHandler, self).__init__(request, client_address, server)
		return

	def setup(self):
		self.logger.debug('setup')
		super(SocketServer.BaseRequestHandler, self).setup()

	def handle(self):
		self.logger.debug('handle')

		# echo the back to the client
		data = self.request.recv(1024)
		self.logger.debug('recv()->"%s"', data)
		self.request.send(data)
		return

	def finish(self):
		self.logger.debug('finish')
		return super(SocketServer.BaseRequestHandler, self).finish(self)

class EchoServer(SocketServer.TCPServer):
	def __init__(self, server_address, handler_class=EchoRequestHandler):
		self.logger = logging.getLogger('EchoServer')
		self.logger.debug('__init__')
		super(EchoServer, self).__init__(server_address, handler_class)
		return

	def server_activate(self):
		self.logger.debug('server_activate')
		super(SocketServer.TCPServer).server_activate(self)
		return

	def serve_forerver(self):
		self.logger.debug('waitting for request')
		self.logger.info('Handling requests, press <Ctrl-C> to quit')
		while True:
			self.handle_request()
		return

	def handle_request(self):
		self.logger.debug("handle_request")
		return super(EchoServer, self).handle_request()

	def verify_request(self, request, client_address):
		self.logger.debug('verify_request(%s, %s)', request, client_address)
		return super(EchoServer, self).verify_request()

	def process_request(self, request, client_address):
		self.logger.debug('process_request(%s %s)', request, client_address)
		return super(EchoServer, self).process_request()

	def server_close(self):
		self.logger.debug('server_close')
		return super(EchoServer, self).server_close()

	def finish_request(self, request, client_address):
		self.logger.debug('finish_request(%s, %s)', request, client_address)
		return super(EchoServer, self).finish_request()

	def close_request(self, request, client_address):
		self.logger.debug('close_request(%s, %s)', request, client_address)
		return super(EchoServer, self).close_request()

if __name__ == '__main__':
	import socket
	import threading
	address = ('localhost', 0)
	server = EchoServer(address, EchoRequestHandler)
	ip, port = server.server_address

	t = threading.Thread(target=server.serve_forever)
	t.setDaemon(True)
	t.start()

	logger = logging.getLogger('client')
	logger.info('Server on %s %s', ip, port)

	# Connect to the server
	logger.debug('creating socket')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	logger.debug('connecting to server')
	s.connect((ip, port))

	# Send the data
	message = 'Hello World'
	logger.debug('sending data: "%s"', message)
	len_sent = s.send(message)

	# Receive a response
	logger.debug('waiting for response')
	response = s.recv(len_sent)
	logger.debug('response from server: "%s"', response)

	# Clean up
	logger.debug('closing socket')
	s.close()
	logger.debug('done')
	server.socket.close()
