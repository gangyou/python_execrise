from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver


factory = Factory()
factory.protocol = LineReceiver()

reactor.listenTCP(1234, factory)
reactor.run()
