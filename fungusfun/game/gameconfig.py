TILE_SIZE = 64 # Draw any size, but underneath tiles are always 64 pixels
PLAYER_SIZE = 56
MAX_FALL = 25 # maximum pixels per second of falling
MAX_MOVE = 8 # maximum pps sideways movement
GRAVITY = 1 # pixels per second squared
FRICTION = 1 # pps^2
MOVE_ACCEL = 2 # pps^2
JUMP_ACCEL = 22

# These assertions can be lifted later, but currently the physics engine makes these assumptions
assert(PLAYER_SIZE < TILE_SIZE)
assert(MAX_MOVE < TILE_SIZE)
assert(MAX_FALL < TILE_SIZE)

# These are used for debugging to check certain properties
_JUMP_HEIGHT = JUMP_ACCEL * (JUMP_ACCEL + 1) / (2 * GRAVITY)
_JUMP_TILES = _JUMP_HEIGHT / TILE_SIZE
_JUMP_DIST = 2 * PLAYER_SIZE + 2 * JUMP_ACCEL // GRAVITY * MAX_MOVE
_JUMP_DIST_TILES = _JUMP_DIST / TILE_SIZE