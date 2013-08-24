def function(a, b):
	print a,b

apply(function, ('whither', 'canada?'))
apply(function, (1, 2+3))
apply(function, (), { 'a':'valuea', 'b':'valueb'})
