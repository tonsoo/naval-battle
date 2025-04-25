import random
from dev.dev_mode import dprint
from graphics.widgets.container.container import Container
from models.generics.rect import Rect
from objects.game.tiles.bomb import Bomb
from objects.game.tiles.ship import Ship
from objects.game.tiles.tile import Tile
from objects.game.tiles.water import Water


class Board(Container):
    
    _size:tuple[int, int] = (0, 0)
    _padding:tuple[int, int] = (0, 0)
    _spacing:tuple[int, int] = (0, 0)
    _refresh_board:bool = True
    _tile_dimension:tuple[int, int] = (0, 0)
    _opened:dict[int, bool] = (0, False)
    _ships:int = 5
    _ships_sizes:list[tuple[int, int]] = []
    _has_turn:bool = False
    _tile_map = {}
    _board_grid = []
    
    def __init__(self, size, padding, spacing, ships = 5, ships_sizes = [[2, 4], [3, 2], [4, 1]], x=0, y=0, width=0, height=0):
        self._size = size
        self._padding = padding
        self._spacing = spacing
        self._ships_sizes = list(ships_sizes)

        # 0 = water, 1 = ship, 2 = bomb
        self._board_grid = [[0 for _ in range(size[0])] for _ in range(size[1])]
        
        super().__init__(x, y, width, height, (105, 163, 245), [])

    def has_turn(self):
        return self._has_turn
    
    def give_turn(self):
        self._has_turn = True
        
    def take_turn(self):
        self._has_turn = False
        
    def get_size(self):
        return self._size

    def get_padding(self):
        return self._padding
    
    def get_spacing(self):
        return self._spacing
    
    
    def _is_tile_at(self, tile, x, y):
        if not isinstance(tile, Tile):
            return
        
        _index = tile.get_index()
        return _index[0] == x and _index[1] == y
    
    def get_tile_at(self, x_index, y_index):
        return self._tile_map.get((x_index, y_index))
        # for child in self.get_children():
        #     if isinstance(child, Tile):
        #         x, y = child.get_index()
        #         if x == x_index and y == y_index:
        #             return child
        # return None
    
    
    def get_tile_rect(self, x, y):
        dimension = self._tile_dimension
        return Rect(
            width=dimension[0],
            height=dimension[1],
            x=self._padding[0] + x * dimension[0] + x * self._spacing[0],
            y=self._padding[1] + y * dimension[1] + y * self._spacing[1],
        )
    
    def _start_board_generation(self):
        self._refresh_board = False
        dprint('Generating board')

        self.empty_children()

        width = self.width
        height = self.height

        size = self._size
        padding = self._padding
        spacing = self._spacing
        grid_dimension = (
            width - padding[0] * 2,
            height - padding[1] * 2,
        )

        self._tile_dimension = (
            grid_dimension[0] / max(1, size[0]) - spacing[0] + (spacing[0] / max(1, size[0] - 1)),
            grid_dimension[1] / max(1, size[1]) - spacing[1] + (spacing[1] / max(1, size[1] - 1))
        )
    
    def generate_board(self, has_bombs = True, has_ships = True):
        size = self._size
        
        self._start_board_generation()

        if has_ships:
            self.populate_ships(self._board_grid)

        if has_bombs:
            self.populate_bombs(self._board_grid, random.randint(3, int(size[0] * size[1] * .25)))

        self.create_tiles(self._board_grid)

    def attack_tile(self, tile: Tile):
        if not self._has_turn:
            return
        
        tile.attack(self)
        
    def create_tiles(self, board_grid):
        size = self._size
        self._tile_map = {}

        for y in range(size[1]):
            for x in range(size[0]):
                tile = None
                if board_grid[y][x] == 1:
                    tile = Ship(
                        board=self,
                        x=x,
                        y=y
                    )
                elif board_grid[y][x] == 2:
                    tile = Bomb(
                        board=self,
                        x=x,
                        y=y
                    )
                else:
                    tile = Water(
                        board=self,
                        x=x,
                        y=y
                    )
                    
                if tile != None:
                    self._tile_map[(x, y)] = tile
                    self.add_child(
                        tile.onClick(self.attack_tile)
                    )

    def populate_ships(self, board_grid):
        size = self._size
        
        for ship_size, ship_count in self._ships_sizes:
            for _ in range(ship_count):
                placed = False
                while not placed:
                    vertical = random.choice([True, False])
                    if vertical:
                        x = random.randint(0, size[0] - 1)
                        y = random.randint(0, size[1] - ship_size)
                        if all(board_grid[y + i][x] == 0 for i in range(ship_size)):
                            for i in range(ship_size):
                                board_grid[y + i][x] = 1
                            placed = True
                    else:
                        x = random.randint(0, size[0] - ship_size)
                        y = random.randint(0, size[1] - 1)
                        if all(board_grid[y][x + i] == 0 for i in range(ship_size)):
                            for i in range(ship_size):
                                board_grid[y][x + i] = 1
                            placed = True
            
    def populate_bombs(self, board_grid, bomb_count = 4):
        size = self._size
        
        from math import dist

        def is_adjacent_to_ship(x, y):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < size[0] and 0 <= ny < size[1]:
                        if board_grid[ny][nx] == 1:
                            return True
            return False

        def is_adjacent_to_bomb(x, y):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < size[0] and 0 <= ny < size[1]:
                        if board_grid[ny][nx] == 2:
                            return True
            return False

        def bomb_score(x, y, bombs):
            score = 100
            if is_adjacent_to_ship(x, y):
                score -= 50
            if is_adjacent_to_bomb(x, y):
                score -= 40
            for bx, by in bombs:
                score -= int(10 / (dist((x, y), (bx, by)) + 1e-5))
            return score

        bombs = []
        while len(bombs) < bomb_count:
            candidates = []
            for y in range(size[1]):
                for x in range(size[0]):
                    if board_grid[y][x] == 0:
                        score = bomb_score(x, y, bombs)
                        candidates.append((score, x, y))
            if not candidates:
                break
            candidates.sort(reverse=True)
            _, bx, by = candidates[0]
            board_grid[by][bx] = 2
            bombs.append((bx, by))
            
        return bombs
    
    def refresh_tiles(self):
        pass
        # for child in self.__children:
        #     if isinstance(child, Tile):
        #         if self._has_turn:
        #             child.onClick(self.attack_tile)
        #         else:
        #             child.onClick(lambda _: None)

    def render(self, surface):
        if self._refresh_board:
            self.generate_board()

        return super().render(surface)