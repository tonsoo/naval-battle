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
        
        
    def handleClick(self, event):
        super().handleClick(event)
        
        for child in self.__children:
            rect = Rect(
                x=child.x, y=child.y,
                width=child.width, height=child.height
            )
            
            child_rect = self._calculate_child_rect(child)
            self._mutate_child_rect(child, child_rect)
            
            child.handleClick(event)
            
            self._mutate_child_rect(child, rect)
    
        
    def render(self, surface):
        self_rect = Rect(
            x=self.x, y=self.y,
            width=self.width, height=self.height,
        )
        if self.width == ContainerTraits.WIDTH_AUTO or self.height == ContainerTraits.HEIGHT_AUTO:
            for child in self.__children:
                rect = Rect(
                    x=child.x, y=child.y,
                    width=child.width, height=child.height
                )

                child_rect = self._calculate_child_rect(child)
                
                if child_rect.width > self_rect.width:
                    self_rect.width = child_rect.width

                if child_rect.height > self_rect.height:
                    self_rect.height = child_rect.height

        if self.color != None:
            pygame.draw.rect(
                surface,
                color=self.color,
                rect=[self_rect.x, self_rect.y, self_rect.width, self_rect.height]
            )

        for child in self.__children:
            rect = Rect(
                x=child.x, y=child.y,
                width=child.width, height=child.height
            )
            
            child_rect = self._calculate_child_rect(child)
            render_child = self._mutate_child_rect(child, child_rect)
            
            self.renderIndividualChild(surface=surface, child=render_child)
            
            self._mutate_child_rect(child, rect)

    def _mutate_child_rect(self, child:Widget, rect:Rect) -> Widget:
        child.x = rect.x
        child.y = rect.y

        child.width = rect.width
        child.height = rect.height

        return child

    def _calculate_child_rect(self, child:Widget) -> Rect:
        rect = Rect(
            x=child.x, y=child.y,
            width=child.width, height=child.height
        )

        rect.x = child.x + self.x
        rect.y = child.y + self.y

        if child.width == ContainerTraits.WIDTH_FULL:
            rect.width = self.width

        if child.height == ContainerTraits.HEIGHT_FULL:
            rect.height = self.height

        return rect

    def renderIndividualChild(self, surface:Surface, child:Widget) -> None:
        child.render(surface)