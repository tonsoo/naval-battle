from errors.app.app_not_running import AppNotRunning
from errors.app.app_already_running import AppAlreadyRunning
from core.window import Window
from windows.app_window import AppWindow

class App:
    __window:Window = None
    __title:str
    
    
    
    def __init__(self, title:str = 'New App'):
        self.set_title(title=title)
        
        
    
    def run(self) -> None:
        if self.is_running():
            raise AppAlreadyRunning()
        
        self.__window = AppWindow(self)
        
    def stop(self) -> None:
        if not self.is_running():
            raise AppNotRunning()

        self.__window = None
        
    def refresh(self) -> None:
        if self.__window != None:
            self.__window.reloadScreen()
    
    def is_running(self) -> bool:
        if self.__window is None:
            return False
        
        return self.__window.isWindowOpen()
    
    
    
    def get_window(self) -> Window:
        return self.__window
    
    def get_title(self) -> str:
        return self.__title
    
    def set_title(self, title:str) -> None:
        self.__title = title
        self.refresh()