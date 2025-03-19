from abc import ABC
from pygame import Color, Surface
import pygame
from models.generics.rect import Rect


class Widget(ABC, Rect):

    color:Color



    def __init__(self, x = 0, y = 0, width = 0, height = 0, color:Color = (0,0,0)):
        super().__init__(x, y, width, height)

        self.color = color


    
    def render(self, surface:Surface) -> None:
        pygame.draw.rect(
            surface,
            color=self.color,
            rect=[self.x, self.y, self.width, self.height]
        )