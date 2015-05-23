from fungusfun.game import tiles

class Map:
    """
    Creates a new empty map, everything filled with air except for a bottom row of grass
    """
    def __init__(self, size=(20,10)):
        self.cols, self.rows = size

        # Data is indexed as [col][row]
        self.data = [[tiles.GRASS if r == self.rows - 1 else tiles.AIR
                    for r in range(self.rows)]
                    for c in range(self.cols)]

        self.spawns = [(c, 2) for c in range(self.cols)]

    """ Produces a JSON serializable representation of the map """
    def save(self):
        obj = {
            "cols": self.cols,
            "rows": self.rows,
            "data": self.data,
            "spawns": self.spawns
        }
        return obj

    """ Initializes the map with the object. Replaces any existing map data. """
    def load(self, obj):
        self.cols = obj["cols"]
        self.rows = obj["rows"]
        self.data = obj["data"]
        self.spawns = list(map(tuple, obj["spawns"])) # convert json lists back into tuples

    def onMap(self, pos):
        col, row = pos
        return col >= 0 and row >= 0 and col < self.cols and row < self.rows

    def getTile(self, pos): # returns tile object
        if not self.onMap(pos):
            return None
        col, row = pos
        return tiles.getTile(self.data[col][row])

    def setTile(self, pos, tile):
        if not self.onMap(pos):
            return
        col, row = pos
        self.data[col][row] = tile

    def isSolid(self, pos):
        if not self.onMap(pos):
            return False
        tile = self.getTile(pos)
        return tile["solid"]