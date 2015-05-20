import pygame
from fungusfun.client.states import ClientState
from fungusfun.game.game import Game
from fungusfun.game import player, tiles
from fungusfun.client import gamerender

class StatePlay:
    def __init__(self, client):
        ClientState.__init__(self, client)
        self.font = pygame.font.Font(None, 16)
        self.timer = 0
        self.game = Game()
        self.pid = self.game.addPlayer()

        # add some solid tiles to game for testing
        self.game.m.setTile((3, 8), tiles.GRASS)
        self.game.m.setTile((5, 6), tiles.GRASS)
        self.game.spawnPlayers()

    def handleEvent(self, event):
        pass

    def handlePacket(self, packet):
        pass

    def tick(self, delta):
        self.timer += delta
        while self.timer > 1000 / 60:
            self.timer -= 1000 / 60

            pressed = pygame.key.get_pressed()
            inputs = []
            if pressed[pygame.K_LEFT]: inputs.append(player.MOVE_LEFT)
            if pressed[pygame.K_RIGHT]: inputs.append(player.MOVE_RIGHT)
            if pressed[pygame.K_UP]: inputs.append(player.JUMP)
            if pressed[pygame.K_DOWN]: inputs.append(player.USE_ITEM)
            self.game.players[self.pid].inputs = inputs

            self.game.tick()

    def draw(self, screen):
        screen.fill((255, 255, 255))

        render = gamerender.renderGame(self.game, (0, 0), screen.get_size())
        screen.blit(render, (0, 0))

