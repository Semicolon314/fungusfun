class ClientState:
    def __init__(self, client):
        self.client = client

    def handleEvent(self, event):
        raise NotImplementedError("Class %s doesn't implement handleEvent()" % (self.__class__.__name__))

    def handlePacket(self, packet):
        raise NotImplementedError("Class %s doesn't implement handlePacket()" % (self.__class__.__name__))

    def tick(self, delta):
        raise NotImplementedError("Class %s doesn't implement tick()" % (self.__class__.__name__))

    def draw(self, screen):
        raise NotImplementedError("Class %s doesn't implement draw()" % (self.__class__.__name__))