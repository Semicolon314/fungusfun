from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory

class ServerProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols += 1
        self.factory.connectCallback(self)
        print("Connection made. %d connections active." % self.factory.numProtocols)

    def connectionLost(self, reason):
        self.factory.numProtocols -= 1
        self.factory.disconnectCallback(self)
        print("Connection lost. %d connections active." % self.factory.numProtocols)

    def dataReceived(self, data):
        if self.clientData != None:
            self.clientData.handleData(data)

    def sendData(self, data):
        self.transport.write(data)

class ServerProtocolFactory(Factory):
    def __init__(self, connectCallback, disconnectCallback):
        self.numProtocols = 0
        self.connectCallback = connectCallback
        self.disconnectCallback = disconnectCallback

    def buildProtocol(self, addr):
        return ServerProtocol(self)