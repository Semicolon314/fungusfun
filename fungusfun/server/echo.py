from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class Echo(Protocol):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    def dataReceived(self, data):
        print("Data:", data.decode("utf-8"))
        self.transport.write(data)

class EchoFactory(Factory):
    def __init__(self):
        self.numProtocols = 0

    def buildProtocol(self, addr):
        return Echo(self)

endpoint = TCP4ServerEndpoint(reactor, 31234)
endpoint.listen(EchoFactory())
reactor.run()