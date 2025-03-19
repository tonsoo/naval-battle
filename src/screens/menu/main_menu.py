import string

from pygame import Surface
import pygame
from core.screen import Screen
from graphics.widgets.container import Container


class MainMenu(Screen):


    __container:Container

    
    def __init__(self, identifier:string = None):
        super().__init__(identifier)

        self.__container = Container(width=20, height=20, color=(50, 90, 120))
        self.addWidget(self.__container)

    

    def update(self):
        self.__container.x = self.__container.x + 1