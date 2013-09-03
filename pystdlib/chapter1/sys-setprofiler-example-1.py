import sys

def test(n):
	j = 0;
	for i in range(n):
		j += i
	return n

def profiler(frame, event, arg):
	print event, frame.f_code.co_name, frame.f_lineno, "->", arg

sys.setprofile(profiler)

test(1)