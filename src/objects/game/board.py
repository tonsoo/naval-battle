import random
from dev.dev_mode import dprint
from graphics.widgets.container.container import Container
from models.generics.rect import Rect
from objects.game.tile import Tile, TileType, TileTypes


class Board(Container):
    
    _size:tuple[int, int]
    _padding:tuple[int, int]
    _spacing:tuple[int, int]
    _refresh_board:bool = True
    _tile_dimension:tuple[int, int]
    _opened:dict[int, bool]
    _ships:int
    _ships_sizes:list[tuple[int, int]]
    
    def __init__(self, size, padding, spacing, ships = 5, ships_sizes = [[2, 4], [3, 2], [4, 1]], x=0, y=0, width=0, height=0):
        self._size = size
        self._padding = padding
        self._spacing = spacing
        self._ships_sizes = list(ships_sizes)
        
        super().__init__(x, y, width, height, (105, 163, 245), [])

    def get_size(self):
        return self._size

    def get_padding(self):
        return self._padding
    
    def get_spacing(self):
        return self._spacing
    
    
    
    def get_tile_rect(self, x, y):
        dimension = self._tile_dimension
        return Rect(
            width=dimension[0],
            height=dimension[1],
            x=self._padding[0] + x * dimension[0] + x * self._spacing[0],
            y=self._padding[1] + y * dimension[1] + y * self._spacing[1],
        )
    
    
    def generate_board(self, has_bombs = True, has_ships = True):
        self._refresh_board = False
        dprint('Refreshing board')

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

        # 0 = water, 1 = ship, 2 = bomb
        board_grid = [[0 for _ in range(size[0])] for _ in range(size[1])]

        if has_ships:
            self.populate_ships(board_grid)

        if has_bombs:
            self.populate_bombs(board_grid, random.randint(3, int(size[0] * size[1] * .25)))

        self.create_tiles(board_grid)

    def create_tiles(self, board_grid):
        size = self._size
        
        def attack_tile(tile: Tile):
            tile.attack()

        for y in range(size[1]):
            for x in range(size[0]):
                tile_type = TileTypes.water()
                if board_grid[y][x] == 1:
                    tile_type = TileTypes.ship()
                elif board_grid[y][x] == 2:
                    tile_type = TileTypes.bomb()
                self.add_child(
                    Tile(
                        type=tile_type,
                        board=self,
                        x=x,
                        y=y
                    ).onClick(attack_tile)
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

    def render(self, surface):
        if self._refresh_board:
            self.generate_board()

        return super().render(surface)