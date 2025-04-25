

from abc import ABC, abstractmethod

from dev.dev_mode import dprint
from graphics.widgets.container.container import Container


class Tile(Container, ABC):

    index = 0
    _opened = False
    
    _x_index = 0
    _y_index = 0
    
    def __init__(self, board, x, y):
        self._x_index = x
        self._y_index = y
        self.index = x + y * board._size[0]
        rect = board.get_tile_rect(x, y)
        super().__init__(rect.x, rect.y, rect.width, rect.height, color=(92, 89, 89))

    @abstractmethod
    def revealed_color(self):
        pass
    
    @abstractmethod
    def name(self):
        pass
    
    def get_index(self):
        return (self._x_index, self._y_index)
    
    def on_open(self, board):
        pass
        
    def attack(self, board) -> bool:
        if self._opened:
            print('The tile was already open')
            return False
        
        dprint(f'Opened a {self.name()}')
        self.color = self.revealed_color()
        self._opened = True

        self.on_open(board)

        return True