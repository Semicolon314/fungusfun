import pygame
from fungusfun.client.states import ClientState
from fungusfun.client.states.play import StatePlay

class StateMenu:
    def __init__(self, client):
        ClientState.__init__(self, client)
        self.font = pygame.font.Font(None, 16)
        self.buttonRect = pygame.Rect(100, 100, 200, 50)
        self.animdir = 1

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttonRect.collidepoint(event.pos):
                self.client.state = StatePlay(self.client)

    def handlePacket(self, packet):
        pass

    def tick(self, delta):
        self.buttonRect.x += self.animdir * delta // 10
        if self.buttonRect.x > 500 or self.buttonRect.x < 100:
            self.animdir *= -1
            self.buttonRect.x += self.animdir * delta // 10

    def draw(self, screen):
        screen.fill((0, 0, 0))

        name_render = self.font.render(self.client.name, 1, (255, 255, 255))
        screen.blit(name_render, (5, 5))

        mouse = pygame.mouse.get_pos()
        screen.fill((255, 255, 255) if self.buttonRect.collidepoint(mouse) else (200, 200, 200), self.buttonRect)
