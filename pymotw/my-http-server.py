import socket
import logging

LOGGER = logging.getLogger('My-Http-Server')
HOST = 'localhost'
PORT = 8000

# HTTP Response
# Prepare HTTP response
TEXT_RESPONSE = '''
HTTP/1.x 200 OK  
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
</html>
'''

IMAGE_RESPONSE = '''
HTTP/1.1 200 OK
Content-Type: image/gif

'''
img = open('test.gif', 'rb')
IMAGE_RESPONSE += img.read()
img.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
	s.listen(3)
	conn, addr = s.accept()
	LOGGER.info("Receive connection from %s:%s", *addr)
	header = conn.recv(1024)
	method = header.split(' ')[0]
	print header
	uri = header.split(' ')[1]

	if method == 'GET':
		if uri == '/test.gif':
			content = IMAGE_RESPONSE
		else:
			content = TEXT_RESPONSE

		conn.sendall(content)

	conn.close()
