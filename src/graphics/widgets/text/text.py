from time import sleep
import pygame
from pygame.freetype import Font
from graphics.widgets.text.fonts import Fonts
from graphics.widgets.widget import Widget


class Text(Widget):
    _text:str = ''
    _font:Font = None
    _fontSize:int = 0
    _color:pygame.Color = (0,0,0)

    def __init__(self, text:str='', x=0, y=0, color:pygame.Color = (0,0,0)):
        super().__init__(x, y, 0, 0)

        self._text = text

    def font(self, font:Font):
        self._font = font
        return self
    
    def font_size(self, size:float):
        self._fontSize = size
        return self
    
    def validate_font(self):
        if self._font == None:
            self._font = Fonts.DM_SANS.weights.w400.load(self._fontSize)

    def render(self, surface):
        self.validate_font()
        
        text_surface = self._font.render(self._text, True, self._color)
        surface.blit(text_surface, (self.x, self.y))