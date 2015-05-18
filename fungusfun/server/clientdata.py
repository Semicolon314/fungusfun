import uuid, json, zlib

class ClientData:
    def __init__(self, server, protocol):
        self.server = server
        self.protocol = protocol
        self.id = uuid.uuid4()

    def handleData(self, data):
        packet = json.loads(zlib.decompress(data).decode("utf-8"))
        self.handlePacket(packet)

    def handlePacket(self, packet):
        print(str(self.id) + "\tReceived packet: ", packet)
        # Do things based on type
        if "type" not in packet:
            return # Bad packet
        t = packet["type"]

        if t == "requestname":
            # TODO: actually validate the name
            self.sendPacket({"type": "validatename", "name": packet["name"], "valid": True})

        pass

    def sendPacket(self, packet):
        print(str(self.id) + "\tSending packet: ", packet)
        data = zlib.compress(json.dumps(packet).encode("utf-8"))
        self.protocol.sendData(data)