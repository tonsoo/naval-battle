from objects.game.board import Board


class PcBoard(Board):
    
    def __init__(self, size, padding, spacing, ships=5, ships_sizes=..., x=0, y=0, width=0, height=0):
        super().__init__(size, padding, spacing, ships, ships_sizes, x, y, width, height)