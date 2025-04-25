from objects.game.board import Board
from objects.game.tiles.ship import Ship


class PcBoard(Board):
    
    _game = None
    
    
    def __init__(self, game, size, padding, spacing, ships=5, ships_sizes=..., x=0, y=0, width=0, height=0):
        super().__init__(size, padding, spacing, ships, ships_sizes, x, y, width, height)
        self._game = game

    def on_attacked(self, tile):
        if not isinstance(tile, Ship):
            self._game.next_turn()