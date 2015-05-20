from fungusfun.game import gameconfig
from fungusfun.game.gameconfig import PLAYER_SIZE, TILE_SIZE

import math

# The various inputs that can be applied
MOVE_LEFT = 1
MOVE_RIGHT = 2
JUMP = 3
USE_ITEM = 4

class Player:
    def __init__(self, game, id):
        self.game = game
        self.id = id
        self.pos = None # not spawned
        self.vel = (0, 0)
        self.inputs = []
        self.item = None
        self.falling = False

        self.history = {}

    def spawn(self, pos):
        self.pos = pos
        self.vel = (0, 0)
        self.falling = False
        self.item = None

    def save(self):
        obj = {
            "pos": self.pos,
            "vel": self.vel,
            "inputs": self.inputs,
            "item": self.item,
            "falling": self.falling
        }
        return obj

    def load(self, obj):
        self.pos = tuple(obj["pos"]) if obj["pos"] != None else None
        self.vel = tuple(obj["vel"]) if obj["vel"] != None else None
        self.inputs = obj["inputs"]
        self.item = obj["item"]
        self.falling = obj["falling"]

    def clearHistory(self, olderThan):
        for tickNum in list(self.history.keys()):
            if tickNum < olderThan:
                del self.history[tickNum]

    def tick(self, tickNum):
        # A tick for a player currently takes 7-9ns
        if self.pos != None:
            vx, vy = self.vel
            x, y = self.pos

            # Apply accelerations
            if JUMP in self.inputs and not self.falling:
                self.falling = True
                vy = -gameconfig.JUMP_ACCEL
            self.falling = True
            if self.falling:
                vy = min(gameconfig.MAX_FALL, vy + gameconfig.GRAVITY)
            else:
                vy = 0
            if abs(vx) > gameconfig.FRICTION:
                vx -= math.floor(math.copysign(gameconfig.FRICTION, vx))
            else:
                vx = 0
            if MOVE_LEFT in self.inputs:
                vx -= gameconfig.MOVE_ACCEL
            if MOVE_RIGHT in self.inputs:
                vx += gameconfig.MOVE_ACCEL
            if abs(vx) > gameconfig.MAX_MOVE:
                vx = math.floor(math.copysign(gameconfig.MAX_MOVE, vx))

            # Apply velocities
            if vx < 0:
                if x % TILE_SIZE < -vx: # crossing into a new column
                    top = y // TILE_SIZE
                    bot = (y + PLAYER_SIZE - 1) // TILE_SIZE
                    newcol = (x + vx) // TILE_SIZE
                    if self.game.m.isSolid((newcol, top)) or self.game.m.isSolid((newcol, bot)): # hit a wall
                        x = (newcol + 1) * TILE_SIZE
                        vx = 0
                    else:
                        x += vx
                else:
                    x += vx
            elif vx > 0:
                if (-x - PLAYER_SIZE) % TILE_SIZE < vx:
                    top = y // TILE_SIZE
                    bot = (y + PLAYER_SIZE - 1) // TILE_SIZE
                    newcol = (x + PLAYER_SIZE + vx - 1) // TILE_SIZE
                    if self.game.m.isSolid((newcol, top)) or self.game.m.isSolid((newcol, bot)): # hit a wall
                        x = newcol * TILE_SIZE - PLAYER_SIZE
                        vx = 0
                    else:
                        x += vx
                else:
                    x += vx

            if vy < 0:
                if y % TILE_SIZE < -vy: # crossing into a new row
                    left = x // TILE_SIZE
                    right = (x + PLAYER_SIZE - 1) // TILE_SIZE
                    newrow = (y + vy) // TILE_SIZE
                    if self.game.m.isSolid((left, newrow)) or self.game.m.isSolid((right, newrow)): # hit a wall
                        y = (newrow + 1) * TILE_SIZE
                        vy = 0
                    else:
                        y += vy
                else:
                    y += vy
            elif vy > 0:
                if (-y - PLAYER_SIZE) % TILE_SIZE < vy:
                    left = x // TILE_SIZE
                    right = (x + PLAYER_SIZE - 1) // TILE_SIZE
                    newrow = (y + PLAYER_SIZE + vy - 1) // TILE_SIZE
                    if self.game.m.isSolid((left, newrow)) or self.game.m.isSolid((right, newrow)): # hit a wall
                        y = newrow * TILE_SIZE - PLAYER_SIZE
                        vy = 0
                        self.falling = False
                    else:
                        y += vy
                else:
                    y += vy

            self.vel = (vx, vy)
            self.pos = (x, y)

            # remove jumps and item uses; they aren't held down
            if JUMP in self.inputs: self.inputs.remove(JUMP)
            if USE_ITEM in self.inputs: self.inputs.remove(USE_ITEM)

        # Save state in history
        self.history[tickNum] = self.save()
        # Clear old history
        self.clearHistory(tickNum - 20)
