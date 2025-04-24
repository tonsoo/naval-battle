from abc import ABC
from typing import Callable
from pygame import Surface
from models.generics.rect import Rect


class Widget(ABC, Rect):
    
    _onClick:Callable[[any], None] = None


    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        super().__init__(x, y, width, height)

    def onClick(self, callback:Callable[[any], None]):
        self._onClick = callback
        return self

    def handleClick(self, event) -> None:
        mouse_pos = event.pos
        mX = mouse_pos[0]
        mY = mouse_pos[1]
        
        if mX < self.x or mX > self.x + self.width:
            return
        
        if mY < self.y or mY > self.y + self.height:
            return
        
        if self._onClick != None:
            self._onClick(self)
    
    def render(self, surface:Surface) -> None:
        pass