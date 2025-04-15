import abc
import pygame
import threading

from core.screen import Screen
from core.time import Time
from core.window_data import WindowData
from errors.window.no_screens_registered import NoScreensRegistered

class Window(abc.ABC):
    __windowOpen:bool = False
    __window:pygame.Surface
    __thread:threading.Thread
    __currentScreen:Screen = None


    __windowData:WindowData = None
    

    def __init__(self, width:float = 800, height:float = 600, startIndex:int = 0, backgroundColor=(0,0,0)):
        self.__thread = threading.Thread(target=lambda: self.run())

        if hasattr(Window, 'started') and Window.started:
            Window.started = True
            pygame.init()
        
        self.__windowData = WindowData(
            width=width,
            height=height,
            background=backgroundColor
        )
        self.__window = pygame.display.set_mode((self.getWidth(), self.getHeight()))
        
        self.__windowOpen = True
        
        self.changeScreen(startIndex)

        self.__thread.run()
        


    def getScreens(self) -> list[Screen]:
        raise NotImplementedError()
    

    
    def getData(self) -> WindowData:
        return self.__windowData
    
    def getWidth(self) -> float:
        return self.getData().getWidth()
    
    def getHeight(self) -> float:
        return self.getData().getHeight()
    

    
    def isWindowOpen(self) -> bool:
        return self.__windowOpen
    

    def changeScreen(self, index:Screen) -> None:
        screenList = self.getScreens()
        if screenList.__len__() < 1:
            raise NoScreensRegistered()
            
        clampedValue = min(screenList.__len__() - 1, max(0, index))
        self.__currentScreen = screenList[clampedValue]
        self.__currentScreen.build(self.getData())
    
    
    def run(self):
        while self.isWindowOpen():
            Time.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__windowOpen = False
                    
                    try:
                        self.__thread.join()
                    except:
                        pass
            self.update(self.__currentScreen, self.__window)

            pygame.display.update()
             
    def update(self, screen:Screen, window:pygame.Surface):
        self.__window.fill(self.__windowData.getBackground())

        screen.render(window)
        screen.update()