TILE_SIZE = 64 # Draw any size, but underneath tiles are always 64 pixels
PLAYER_SIZE = 56
MAX_FALL = 16 # maximum pixels per second of falling
MAX_MOVE = 10 # maximum pps sideways movement
GRAVITY = 0.7 # pixels per second squared
FRICTION_GROUND = 2.0 # pps^2
FRICTION_AIR = 1.3
JUMP_ACCEL = 16
MAX_JUMP = 10

# These assertions can be lifted later, but currently the physics engine makes these assumptions
assert(PLAYER_SIZE < TILE_SIZE)
assert(MAX_MOVE < TILE_SIZE)
assert(MAX_FALL < TILE_SIZE)

# These are used for debugging to check certain properties
_JUMP_HEIGHT = JUMP_ACCEL * (JUMP_ACCEL + 1) / (2 * GRAVITY)
_JUMP_TILES = _JUMP_HEIGHT / TILE_SIZE
_JUMP_DIST = 2 * PLAYER_SIZE + 2 * JUMP_ACCEL // GRAVITY * MAX_MOVE
_JUMP_DIST_TILES = _JUMP_DIST / TILE_SIZE