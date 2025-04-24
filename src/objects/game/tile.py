

from enum import Enum

from pygame import Color
from dev.dev_mode import dprint
from graphics.widgets.container.container import Container


class Tile(Container):

    index = 0
    _opened = False
    _type = None
    
    def __init__(self, type, board, x, y):
        self.index = x + y * board._size[0]
        rect = board.get_tile_rect(x, y)
        self._type = type
        print(f'type: {type}')
        super().__init__(rect.x, rect.y, rect.width, rect.height, color=(92, 89, 89))
        
    def attack(self) -> bool:
        if self._opened:
            print('The tile was already open')
            return False
            
        dprint(f'Opened a {self._type.name()}')
        self.color = self._type.color()
        self._opened = True

        return True
    
class TileType:
    _opened_color:Color
    _name:str
    
    def __init__(self, name, color = (43, 40, 40)):
        self._opened_color = color
        self._name = name
        
    def color(self):
        return self._opened_color
    
    def name(self):
        return self._name
    
class TileTypes:
    
    def water():
        return TileType('tile.water', (45, 101, 196))
    
    def ship():
        return TileType('tile.ship', (173, 120, 50))
    
    def bomb():
        return TileType('tile.bomb', (163, 64, 57))