_tileMap = {}

def createTile(id, solid=True, sheet=None, sheetPos=(0,0)):
    tile = {
        "id": id,
        "solid": solid,
        "sheet": sheet,
        "sheetPos": sheetPos
    }
    _tileMap[id] = tile
    return id

def getTile(id):
    return _tileMap[id] if id in _tileMap else None

TILE_AIR = createTile(0, solid=False)
TILE_GRASS = createTile(1, solid=True)