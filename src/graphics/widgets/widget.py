from abc import ABC
from pygame import Surface
from models.generics.rect import Rect


class Widget(ABC, Rect):


    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        super().__init__(x, y, width, height)


    
    def render(self, surface:Surface) -> None:
        pass