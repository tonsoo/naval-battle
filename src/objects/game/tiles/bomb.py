from math import sqrt
from objects.game.tiles.tile import Tile


class Bomb(Tile):
    def __init__(self, board, x, y):
        super().__init__(board, x, y)

    def name(self):
        return 'bomb'
    
    def revealed_color(self):
        return (163, 64, 57)
    
    def on_open(self, board):
        print('on open bomb aa')
        radius = 2
        for x_add in range(-radius, radius + 1):
            for y_add in range(-radius, radius + 1):
                if x_add**2 + y_add**2 <= radius**2:
                    tile = board.get_tile_at(
                        self._x_index + x_add,
                        self._y_index + y_add,
                    )
                    if tile is not None:
                        tile.attack(board)