from pygame import Color, Surface
import pygame
from graphics.widgets.container.container_traits import ContainerTraits
from graphics.widgets.widget import Widget
from models.generics.rect import Rect


class Container(Widget):


    color:Color
    __children:list[Widget]
    

    def __init__(self, x=0, y=0, width=0, height=0, color:Color = (0,0,0), children:list[Widget] = []):
        super().__init__(x, y, width, height)
        
        self.color = color
        self.__children = children
        
        
        
    def render(self, surface):
        pygame.draw.rect(
            surface,
            color=self.color,
            rect=[self.x, self.y, self.width, self.height]
        )

        for child in self.__children:
            rect = Rect(
                x=child.x, y=child.y,
                width=child.width, height=child.height
            )

            child.x = child.x + self.x
            child.y = child.y + self.y

            if child.width == ContainerTraits.WIDTH_FULL:
                child.width = self.width

            if child.height == ContainerTraits.HEIGHT_FULL:
                child.height = self.height
            
            self.renderIndividualChild(surface=surface, child=child)
            
            child.x = rect.x
            child.y = rect.y

            child.width = rect.width
            child.height = rect.height

    def renderIndividualChild(self, surface:Surface, child:Widget) -> None:
        child.render(surface)