import pygame
from fungusfun.client.states import ClientState
from fungusfun.client.states.menu import StateMenu

# State is currently very sketchy but demonstrates structure of a client state
class StateConnecting(ClientState):
    def __init__(self, client):
        ClientState.__init__(self, client)
        self.text = ""
        self.error = ""
        self.font = pygame.font.Font(None, 20)
        self.fg_color = pygame.Color(255, 255, 255)

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if self.text != None:
                if event.key == pygame.K_BACKSPACE:
                    if len(self.text) > 0:
                        self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    if not self.client.netman.isConnected():
                        self.client.netman.connect(self.text, 31234)
                        self.text = None
                    else:
                        self.client.netman.sendPacket({"type": "requestname", "name": self.text})
                else:
                    self.text += event.unicode

    def handlePacket(self, packet):
        t = packet["type"]

        if t == "validatename":
            if packet["valid"]:
                self.client.name = packet["name"]
                self.client.state = StateMenu(self.client)
            else:
                if packet["reason"] == "regex":
                    self.error = "Name must be 3-20 alphanumeric characters."
                elif packet["reason"] == "inuse":
                    self.error = "Name is in use."
                else:
                    self.error = "Invalid name."

        pass

    def tick(self, delta):
        if self.client.netman.isConnected():
            if self.text == None:
                self.text = ""

    def draw(self, screen):
        screen.fill((0, 0, 0))

        instruction_render = self.font.render("Enter server address:" if not self.client.netman.isConnected() else "Enter name:", 1, self.fg_color)
        addr_render = self.font.render(self.text if self.text != None else "Connecting...", 1, self.fg_color)
        error_render = self.font.render(self.error, 1, (255, 0, 0))

        screen.blit(instruction_render, ((screen.get_width() - instruction_render.get_width()) / 2, 50))
        screen.blit(addr_render, ((screen.get_width() - addr_render.get_width()) / 2, 100))
        screen.blit(error_render, ((screen.get_width() - error_render.get_width()) / 2, 200))
