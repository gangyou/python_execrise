import md5, string, random

def getchallenge():
	challenge = map(lambda i: chr(random.randint(0 ,255)), range(16))
	return string.join(challenge, "")

def getresponse(password, challenge):
	m = md5.new()
	m.update(password)
	m.update(challenge)
	return m.digest()

# server/client communication

# 1. client connects. server issues challenge

print "client:", "connect"

challenge = getchallenge()

print "server:", repr(challenge)

# 2. client combines password and challenge, and calculates
client_response = getresponse("trustno1", challenge)

print "client:", repr(client_response)

# 3. server does the same, and compares the result with the client response.
# the result is a safe login in which the pasword is never sent across the communication channel.
server_response = getresponse("trustno1", challenge)

if server_response == client_response:
	print "server:", "login ok"