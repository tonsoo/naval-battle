import abc
import pygame
import threading

from core.screen import Screen
from errors.window.no_screens_registered import NoScreensRegistered

class Window(abc.ABC):
    __windowOpen:bool = False
    __window:pygame.Surface
    __thread:threading.Thread
    __currentScreen:Screen
    

    def __init__(self, width:float = 800, height:float = 600, startScreenIndex:int=1):
        self.__thread = threading.Thread(target=lambda: self.run())

        if hasattr(Window, 'started') and Window.started:
            Window.started = True
            pygame.init()
            
        screenList = self.getScreens()
        if screenList.__len__() < 1:
            raise NoScreensRegistered()
            
        clampedValue = min(screenList.__len__() - 1, max(0, startScreenIndex))
        self.__currentScreen = screenList[clampedValue]
        
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
                    
            self.__currentScreen.render(self.__window)
                    
            self.update(self.__currentScreen, self.__window)
             
    def update(self, screen:Screen, window:pygame.Surface):
        pass