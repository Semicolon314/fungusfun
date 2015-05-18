import sys, os
import pygame
from fungusfun import config
from fungusfun.client.netman import Netman

# TODO: refactor importing of client states (package?)
from fungusfun.client.states.connecting import StateConnecting

class Client:
    def __init__(self):
        pygame.init()

        icon = pygame.image.load(os.path.join("fungusfun", "client", "assets", "icon.png"))
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode(config.DEFAULT_CLIENT_SIZE)
        pygame.display.set_caption("Fungus Fun")

        self.lastTick = pygame.time.get_ticks()
        self.netman = Netman()
        self.state = StateConnecting(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.netman.shutdown()
                    sys.exit()
                self.handleEvent(event)
            for packet in self.netman.getPackets():
                self.handlePacket(packet)
            self.tick()
            self.draw()

    def handleEvent(self, event):
        self.state.handleEvent(event)

    def handlePacket(self, packet):
        self.state.handlePacket(packet)

    def tick(self):
        delta = pygame.time.get_ticks() - self.lastTick
        self.lastTick = pygame.time.get_ticks()

        self.state.tick(delta)

    def draw(self):
        self.state.draw(self.screen)

        pygame.display.flip()
