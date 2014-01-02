# Socket server example in python

import socket
import sys
from thread import *

HOST = ''
PORT = 8888

s = socket.socket()
print 'Socket created'

try:
	s.bind((HOST, PORT))
except socket.error, msg:
	print 'Bind failed. Error Code :' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listining'

# Function for handling connections. This will be used to creat threads
def clientthread(conn):
	# Sending message to connected client
	conn.send('Welcome to the server. Type something and hit enter\n')

	# infinite loop so that function do not terminate and thread do not end
	while True:
		# Receiving from client
		data = conn.recv(1024)
		reply = 'OK...' + data
		if not data:
			break

		conn.sendall(reply)

	conn.close()

# now keep talking with the client
while True:
	# wait to accept a connection - blocking call
	conn, addr = s.accept()
	print 'Connected with ' + addr[0] + ':' + str(addr[1])

	# start new thread takes 1st arguments as a function name to be run, second is the tuple of arguments to the function
	start_new_thread(clientthread, (conn,))

s.close()

