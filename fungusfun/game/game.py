from fungusfun.game.map import Map
from fungusfun.game.player import Player
from fungusfun.game import gameconfig

import random

"""
Stores all data about a game in progress, including players, maps, and items
"""
class Game:
    """
    settings is currently just used for the map. It will be used for items and physics later.
    serverMode tells the game that it can make its own random decisions and discard history
    """
    def __init__(self, settings={}, serverMode=True):
        self.m = Map()
        if "map" in settings:
            self.m.load(settings["map"])
        self.players = {}
        self.playerId = 0
        self.serverMode = serverMode
        self.tickNum = 0

    def addPlayer(self):
        self.playerId += 1
        player = Player(self, self.playerId)
        self.players[player.id] = player
        return player.id

    def removePlayer(self, id):
        del self.players[id]

    """ Spawns any players not already spawned (server mode only) """
    def spawnPlayers(self):
        if not self.serverMode:
            return
        for player in self.players.values():
            if player.pos == None:
                player.spawn(random.choice(self.m.spawns))

    def tick(self):
        # iterate through players in order by id
        for id, player in sorted(self.players.items()):
            player.tick(self.tickNum)

        self.tickNum += 1