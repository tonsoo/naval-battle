import string

from pygame import Surface
import pygame
from core.screen import Screen
from core.time import Time
from graphics.widgets.container import Container


class MainMenu(Screen):


    __container:Container
    __speed:float = 100

    
    def __init__(self, identifier:string = None):
        super().__init__(identifier)

        self.__container = Container(width=20, height=20, color=(50, 90, 120))
        self.addWidget(self.__container)

    

    def update(self):
        self.handleMovement()



    def move_container(self, x:float = 0, y:float = 0) -> None:
        self.__container.x = self.__container.x + x * Time.deltaTime()
        self.__container.y = self.__container.y + y * Time.deltaTime()


    
    def handleMovement(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_container(x=-self.__speed)
        elif keys[pygame.K_RIGHT]:
            self.move_container(x=self.__speed)

        if keys[pygame.K_UP]:
            self.move_container(y=-self.__speed)
        elif keys[pygame.K_DOWN]:
            self.move_container(y=self.__speed)