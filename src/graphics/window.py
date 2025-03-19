import pygame
import threading

class Window(threading.Thread):
    __windowOpen:bool = False
    

    def __init__(self, width:float = 800, height:float = 600):
        threading.Thread.__init__(self)

        if hasattr(Window, 'started') and Window.started:
            Window.started = True
            pygame.init()
        
        pygame.display.set_mode((width, height))
        
        self.__windowOpen = True
        self.start()
        

    
    def isWindowOpen(self) -> bool:
        return self.__windowOpen
    
    
    def run(self):
        while self.isWindowOpen():
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.__windowOpen = False