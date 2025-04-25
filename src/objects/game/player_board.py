from dev.dev_mode import dprint
from objects.game.board import Board


class PlayerBoard(Board):
    def __init__(self, size, padding, spacing, ships=5, ships_sizes=[[2, 4], [3, 2], [4, 1]], x=0, y=0, width=0, height=0):
        super().__init__(size, padding, spacing, ships, ships_sizes, x, y, width, height)

    def generate_board(self):
        self._start_board_generation()
        
        self.create_tiles(self._board_grid)

    def place_ship(self, x, y, vertical, length):
        if vertical:
            if y + length > self._size[1]:
                return False
            if any(self._board_grid[y + i][x] != 0 for i in range(length)):
                return False
            for i in range(length):
                self._board_grid[y + i][x] = 1
        else:
            if x + length > self._size[0]:
                return False
            if any(self._board_grid[y][x + i] != 0 for i in range(length)):
                return False
            for i in range(length):
                self._board_grid[y][x + i] = 1

        self.create_tiles(self._board_grid)
        return True
