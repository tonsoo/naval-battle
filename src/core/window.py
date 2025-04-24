import abc
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
    

    def __init__(self, app, width:float = 800, height:float = 600, startIndex:int = 0, backgroundColor=(0,0,0)):
        self.__thread = threading.Thread(target=self.run)
        
        self.__windowData = WindowData(
            app=app,
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
    
    def reloadScreen(self) -> None:
        screen = None
        
        
        screenList = self.getScreens()
        i = 0
        for _ in screenList:
            if _.id() == self.__currentScreen.id():
                screen = _
                break
            i = i + 1
            
        if screen != None:
            self.changeScreen(i)
        else:
            print('Failed to find screen')
    
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

            events = pygame.event.get()
            DevMode.update(events)
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.__windowOpen = False
                    
                    try:
                        self.__thread.join()
                    except:
                        pass
                    
                self.propagateEvent(event, self.__currentScreen)
                        
            self.update(self.__currentScreen, self.__window)

            pygame.display.update()
             
    def propagateEvent(self, event, screen:Screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                screen.handleClick(event)
        
    def update(self, screen:Screen, window:pygame.Surface):
        self.__window.fill(self.__windowData.getBackground())

        screen.render(window)
        screen.update()