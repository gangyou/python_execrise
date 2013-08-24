import os
import time

pid = os.fork()
if pid:
	os._exit(0)

print "daemon started"
time.sleep(10)
print "daemon terminated"