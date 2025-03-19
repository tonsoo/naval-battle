import string

from pygame import Surface
import pygame
from core.screen import Screen
from graphics.widgets.container import Container


class MainMenu(Screen):
    
    def __init__(self, identifier:string = None):
        super().__init__(identifier)

        self.addWidget(Container(width=20, height=20, color=(50, 90, 120)))