from dev.dev_mode import dprint
from objects.game.board import Board


class PlayerBoard(Board):
    
    _interactable = False
    _game = None
    remaining = []
    
    def __init__(self, game, size, padding, spacing, ships=5, ships_sizes=[[2, 4], [3, 2], [4, 1]], x=0, y=0, width=0, height=0):
        super().__init__(size, padding, spacing, ships, ships_sizes, x, y, width, height)

        self._game = game
        self.remaining = [(_x, _y) for _x in range(size[0]) for _y in range(size[1])]
        print(self.remaining)

    # def on_attacked(self):
    #     self._game.next_turn()
        
    def generate_board(self):
        self._start_board_generation()
        
        self.create_tiles(self._board_grid)
        
    def generate_board_with_bombs(self):
        self.populate_bombs(self._board_grid)
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
    
    def get_tile_size(self):
        pad_x, pad_y = self._padding
        space_x, space_y = self._spacing
        cell_w = (self.width - pad_x * 2 - space_x * (self._size[0] - 1)) / self._size[0]
        cell_h = (self.height - pad_y * 2 - space_y * (self._size[1] - 1)) / self._size[1]
        return (cell_w, cell_h)

    def grid_to_screen(self, tile_x, tile_y):
        cell_w, cell_h = self.get_tile_size()
        pad_x, pad_y = self._padding
        space_x, space_y = self._spacing

        x = self.x + pad_x + tile_x * (cell_w + space_x)
        y = self.y + pad_y + tile_y * (cell_h + space_y)
        return x, y

    def find_nearest_tile(self, px, py):
        cell_w, cell_h = self.get_tile_size()
        for y in range(self._size[1]):
            for x in range(self._size[0]):
                sx, sy = self.grid_to_screen(x, y)
                if sx - 5 <= px <= sx + cell_w + 5 and sy - 5 <= py <= sy + cell_h + 5:
                    return (x, y)
        return None