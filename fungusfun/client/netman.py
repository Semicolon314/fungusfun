# Connects to the server and converts packets to and from JSON for transmission
# Stores received packets until they can be handled sychronously by the client

from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from threading import Thread

import json

class ClientProtocol(Protocol):
    def __init__(self, netman):
        self.netman = netman

    def dataReceived(self, data):
        self.netman.handleData(data)

    def sendData(self, data):
        self.transport.write(data)

    def disconnect(self):
        self.transport.loseConnection()

class Netman:
    def __init__(self):
        self.packets = []
        self.protocol = None

    def connect(self, host, port):
        point = TCP4ClientEndpoint(reactor, host, port)
        d = connectProtocol(point, ClientProtocol(self))
        d.addCallback(self.gotProtocol)
        self.t = Thread(target=reactor.run, args=(False,)).start()

    def gotProtocol(self, protocol):
        self.protocol = protocol

    def isConnected(self):
        return self.protocol != None

    def handleData(self, data):
        packet = json.loads(data.decode("utf-8"))
        self.packets.append(packet)

    def sendPacket(self, packet):
        if self.protocol != None:
            data = json.dumps(packet).encode("utf-8")
            reactor.callFromThread(self.protocol.sendData, data)

    def disconnect(self):
        reactor.callFromThread(self.protocol.disconnect)
        reactor.callFromThread(reactor.stop)

    def getPackets(self):
        packets = self.packets
        self.packets = []
        return packets