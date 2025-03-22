from pygame import Color
import pygame
from graphics.widgets.widget import Widget


class Container(Widget):


    color:Color
    
    

    def __init__(self, x=0, y=0, width=0, height=0, color:Color = (0,0,0)):
        super().__init__(x, y, width, height, color)
        
        self.color = color
        
        
        
    def render(self, surface):
        pygame.draw.rect(
            surface,
            color=self.color,
            rect=[self.x, self.y, self.width, self.height]
        )