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
        self.handleMovement()



    def move_container(self, x:float = 0, y:float = 0) -> None:
        self.__container.x = self.__container.x + x
        self.__container.y = self.__container.y + y


    
    def handleMovement(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_container(x=-1)
        elif keys[pygame.K_RIGHT]:
            self.move_container(x=1)

        if keys[pygame.K_UP]:
            self.move_container(y=-1)
        elif keys[pygame.K_DOWN]:
            self.move_container(y=1)