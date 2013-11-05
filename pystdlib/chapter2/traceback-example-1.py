import traceback

try:
	raise SyntaxError, "example"
except:
	traceback.print_exc()

