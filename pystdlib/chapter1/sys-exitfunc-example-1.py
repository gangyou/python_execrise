import sys

def exitfunc():
	print "world"

sys.exitfunc = exitfunc

print "hello"

sys.exit(1)

# never print
print "there"

# 在 Python 2.0 以后, 你可以使用 atexit 模块来注册多个退出处理函数.