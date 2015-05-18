from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

from fungusfun.server.protocol import ServerProtocolFactory
from fungusfun.server.clientdata import ClientData

class Server:
    def __init__(self, port):
        self.port = port
        self.clients = []

    def connectClient(self, protocol):
        cd = ClientData(self, protocol)
        protocol.clientData = cd
        self.clients.append(cd)

    def disconnectClient(self, protocol):
        self.clients.remove(protocol.clientData)

    def run(self):
        endpoint = TCP4ServerEndpoint(reactor, self.port)
        endpoint.listen(ServerProtocolFactory(self.connectClient, self.disconnectClient))
        reactor.run()