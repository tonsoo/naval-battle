import abc
from ctypes.wintypes import PULARGE_INTEGER
import pygame
import threading

from core.screen import Screen
from core.time import Time
from core.window_data import WindowData
from dev.dev_mode import DevMode, dprint
from errors.window.no_screens_registered import NoScreensRegistered

class Window(abc.ABC):
    __windowOpen:bool = False
    __window:pygame.Surface
    __thread:threading.Thread
    __currentScreen:Screen = None
    __currentScreenIsBuilt:bool = False


    __windowData:WindowData = None
    

    def __init__(self, width:float = 800, height:float = 600, startIndex:int = 0, backgroundColor=(0,0,0)):
        self.__thread = threading.Thread(target=self.run)
        
        self.__windowData = WindowData(
            width=width,
            height=height,
            background=backgroundColor
        )
        
        self.changeScreen(startIndex)

        self.__thread.start()
        


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
        self.__currentScreenIsBuilt = False
    
    
    def openWindow(self):
        driver = pygame.display.get_driver()
        flags = 0
        if driver == "opengl":
            flags = pygame.OPENGL
        elif driver == "directx":
            flags = pygame.SWSURFACE
        
        self.__window = pygame.display.set_mode((self.getWidth(), self.getHeight()), flags)
        
        self.__windowOpen = True
        
    
    def run(self):
        pygame.init()
        pygame.font.init()
        
        self.openWindow()
        
        while self.isWindowOpen():
            Time.update()
            
            if not pygame.display.get_init() or not pygame.font.get_init():
                dprint('skipping :p')
                continue
            
            if not self.__currentScreenIsBuilt:
                self.__currentScreen.build(self.getData())
                self.__currentScreenIsBuilt = True
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__windowOpen = False
                    
                    try:
                        DevMode.stop()
                        self.__thread.join()
                        self.__windowOpen = False
                    except:
                        pass
            self.update(self.__currentScreen, self.__window)

            pygame.display.update()
             
    def update(self, screen:Screen, window:pygame.Surface):
        self.__window.fill(self.__windowData.getBackground())

        screen.render(window)
        screen.update()