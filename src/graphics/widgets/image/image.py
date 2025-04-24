import pygame
from graphics.widgets.widget import Widget


class Image(Widget):
    
    _src:str
    _image = None
    
    def __init__(self, src:str, x=0, y=0, width=0, height=0):
        super().__init__(x, y, width, height)

        self._src = src
        self._image = pygame.image.load(src)
        self._image = pygame.transform.scale(self._image, (width, height))

    
    def render(self, surface):
        surface.blit(self._image, (self.x, self.y))