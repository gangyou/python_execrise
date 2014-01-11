from twisted.internet.defer import Deferred

def callback(res):
    raise Exception('oops')

def errback(resson):
	print resson.getErrorMessage()

d = Deferred()

d.addCallbacks(callback, errback)
d.addCallbacks(callback, errback)
d.callback('Here is your result.')

print "Finished"
