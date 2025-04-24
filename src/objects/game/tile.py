

from graphics.widgets.container.container import Container


class Tile(Container):

    index = 0
    _opened = False
    
    def __init__(self, board, x, y):
        self.index = x + y * board._size[0]
        rect = board.get_tile_rect(x, y)
        super().__init__(rect.x, rect.y, rect.width, rect.height, color=(92, 89, 89))
        
    def attack(self) -> bool:
        if self._opened:
            print('The tile was already open')
            return False
            
        self.color = (43, 40, 40)

        return True