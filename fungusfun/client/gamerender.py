import pygame
from fungusfun.game.gameconfig import TILE_SIZE
from fungusfun.client.assetman import getImage
from fungusfun.game.tiles import getTile

tileSheet = getImage("tiles.png")
testPlayer = getImage("playertest.png")

def getTileRect(tile):
    if tile == None or tile["sheetPos"][0] == -1:
        return pygame.Rect(0, 0, 0, 0)
    else:
        return pygame.Rect(tile["sheetPos"][0] * TILE_SIZE, tile["sheetPos"][1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)

"""
Renders a portion of the map onto a surface
The portion starts from pos=(x,y) and will be size=(width,height)
"""
def renderMap(m, pos, size):
    s = pygame.Surface(size, pygame.SRCALPHA)
    s.fill((0, 0, 0, 0)) # fully transparent

    x, y = pos
    width, height = size

    for c in range(m.cols):
        # check if this column is visible
        if (c + 1) * TILE_SIZE > x and c * TILE_SIZE <= x + width:
            for r in range(m.rows):
                # check if this row is visible
                if (r + 1) * TILE_SIZE > y and r * TILE_SIZE <= y + height:
                    rect = getTileRect(m.getTile((c, r)))
                    s.blit(tileSheet, (c * TILE_SIZE - x, r * TILE_SIZE - y), rect)

    return s

def renderGame(game, pos, size):
    s = renderMap(game.m, pos, size)

    for player in game.players.values():
        s.blit(testPlayer, player.pos)

    return s
