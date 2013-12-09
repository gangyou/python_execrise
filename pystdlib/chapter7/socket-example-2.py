import socket, struct, time

port = 8037

time1970 = 2208988800L

service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
service.bind(("", port))
service.listen(1)

print 'listening on port', port 

while 1:
	channel, info = service.accept()
	print 'connection from', info
	t = int(time.time()) + time1970
	t = struct.pack("!I", t)
	channel.send(t)
	channel.close()