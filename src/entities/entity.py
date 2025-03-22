from abc import abstractmethod

from graphics.widgets.widget import Widget


class Entity(Widget):
    
    _speed:float
    
    def __init__(self, x = 0, y = 0, width = 0, height = 0, speed:float=100):
        super().__init__(x, y, width, height)
        
        self._speed = speed
        
    
    
    @abstractmethod
    def tick(self):
        pass