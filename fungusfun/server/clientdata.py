import uuid, json, zlib

class ClientData:
    def __init__(self, server, protocol):
        self.server = server
        self.protocol = protocol
        self.id = uuid.uuid4()
        self.name = None

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
            if self.name == None:
                valid = self.server.validName(packet["name"])
                obj = {"type": "validatename", "name": packet["name"], "valid": valid == "valid"}
                if valid == "valid":
                    self.name = packet["name"]
                else:
                    obj["reason"] = valid
                self.sendPacket(obj)

        pass

    def sendPacket(self, packet):
        print(str(self.id) + "\tSending packet: ", packet)
        data = zlib.compress(json.dumps(packet).encode("utf-8"))
        self.protocol.sendData(data)
