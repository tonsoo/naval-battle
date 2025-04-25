from math import sqrt
from objects.game.tiles.tile import Tile


class Water(Tile):
    def __init__(self, board, x, y):
        super().__init__(board, x, y)

    def name(self):
        return 'water'
    
    def revealed_color(self):
        return (45, 101, 196)
    
    def on_open(self, board):
        pass