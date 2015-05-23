_tileMap = {}

def createTile(id, solid=True, sheetPos=(0,0)):
    tile = {
        "id": id,
        "solid": solid,
        "sheetPos": sheetPos
    }
    _tileMap[id] = tile
    return id

def getTile(id):
    return _tileMap[id] if id in _tileMap else None

AIR = createTile(0, solid=False, sheetPos=(-1,-1)) # no image
GRASS = createTile(1, solid=True, sheetPos=(0,0))