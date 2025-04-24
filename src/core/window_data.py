from turtle import back
import pygame


class WindowData:
    __backgroundColor:pygame.Color

    __width:float
    __height:float
    
    __app = None

    def __init__(self, app, width:float, height:float, background:pygame.Color):
        self.__backgroundColor = background
        self.__width = width
        self.__height = height
        self.__app = app

    

    def getApp(self):
        return self.__app
    
    def getWidth(self) -> float:
        return self.__width
    
    def getHeight(self) -> float:
        return self.__height
    
    def getBackground(self) -> pygame.Color:
        return self.__backgroundColor