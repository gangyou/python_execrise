import os,signal, time

def signal_usr1(signum, frame):
	pid = os.getpid()
	print 'Received USR1 in process %s' % pid

print 'Forking...'
child_pid = os.fork()
if child_pid:
	print 'PARENT: Pausing before sending signal...'
	time.sleep(1)
	print 'PARENT: Signaling %s' % child_pid
	os.kill(child_pid, signal.SIGUSR1)
else:
	print 'CHILD: Setting up signal handler'
	signal.signal(signal.SIGUSR1, signal_usr1)
	print 'CHILD: Pausong to wait for signal'
	time.sleep(5)