import os

parent_pid = os.getpid()
print '[parent] starts PID: %d' % (parent_pid,)

forked_pid = os.fork()
if forked_pid == 0:
	print '[child] child process can\'t use os.fork() PID, since it\'s %d' % (forked_pid, )
	print "[child] but it can reevaluate os.getpid() to get it's own PID: %d" % (os.getpid(), )
else:
	print "[parent] parent process have createed child with PID: %d" % (forked_pid, )