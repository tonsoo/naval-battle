import abc
from turtle import Screen
import pygame
import threading

class Window(abc.ABC):
    __windowOpen:bool = False
    __window:pygame.Surface
    __thread:threading.Thread
    

    def __init__(self, width:float = 800, height:float = 600):
        self.__thread = threading.Thread(target=lambda: self.run())

        if hasattr(Window, 'started') and Window.started:
            Window.started = True
            pygame.init()
        
        self.__window = pygame.display.set_mode((width, height))
        
        self.__windowOpen = True
        
        self.__thread.run()
        


    def getScreens(self) -> list[Screen]:
        raise NotImplementedError()
    

    
    def isWindowOpen(self) -> bool:
        return self.__windowOpen
    
    
    def run(self):
        while self.isWindowOpen():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__windowOpen = False
                    
                    try:
                        self.__thread.join()
                    except:
                        pass

            self.update()
             
    def update(self):
        pass