import sys

def test(n):
	j = 0;
	for i in range(n):
		j += i
	return n

def tracer(frame, event, arg):
	print event, frame.f_code.co_name, frame.f_lineno, "->", arg
	return tracer

sys.settrace(tracer)

test(1)