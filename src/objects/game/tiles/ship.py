from objects.game.tiles.tile import Tile


class Ship(Tile):
    def __init__(self, board, x, y):
        super().__init__(board, x, y)

    def name(self):
        return 'ship'
    
    def revealed_color(self):
        return (173, 120, 50)