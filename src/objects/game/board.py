from dev.dev_mode import dprint
from graphics.widgets.container.container import Container
from models.generics.rect import Rect
from objects.game.tile import Tile


class Board(Container):
    
    _size:tuple[int, int]
    _padding:tuple[int, int]
    _spacing:tuple[int, int]
    _refresh_board:bool = True
    _tile_dimension:tuple[int, int]
    _opened:list[int]
    
    def __init__(self, size, padding, spacing, x=0, y=0, width=0, height=0):
        self._size = size
        self._padding = padding
        self._spacing = spacing
        
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
    
    
    def generate_board(self):
        self._refresh_board = False
        dprint('Refreshing board')
        
        self.empty_children()
        
        width = self.width
        height = self.height
        
        size = self._size
        padding = self._padding
        grid_dimension = (
            width - padding[0] * 2,
            height - padding[1] * 2,
        )

        spacing = self._spacing
        self._tile_dimension = (
            grid_dimension[0] / max(1, size[0]) - spacing[0] + (spacing[0] / max(1, size[0] - 1)),
            grid_dimension[1] / max(1, size[1]) - spacing[1] + (spacing[1] / max(1, size[1] - 1))
        )
        
        def attack_tile(tile:Tile):
            tile.attack()
            # if tile.attack():
            #     self._refresh_board = True
        
        for _x in range(0, size[0]):
            for _y in range(0, size[1]):
                self.add_child(
                    Tile(
                        board=self,
                        x=_x,
                        y=_y
                    ).onClick(attack_tile)
                )

    def render(self, surface):
        if self._refresh_board:
            self.generate_board()

        return super().render(surface)