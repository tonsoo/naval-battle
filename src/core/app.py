from src.errors.app.app_not_running import AppNotRunning
from src.errors.app.app_already_running import AppAlreadyRunning

class App:
    __running:bool = False
    __title:str
    
    
    
    def __init__(self, title:str = 'New App'):
        self.set_title(title=title)
        
        
    
    def run(self) -> bool:
        if self.is_running():
            raise AppAlreadyRunning()
        
        self.__running = True
        
    def stop(self) -> bool:
        if not self.is_running():
            raise AppNotRunning()

        self.__running = False
    
    def is_running(self) -> bool:
        return self.__running
    
    
    
    def get_title(self) -> str:
        return self.__title
    
    def set_title(self, title:str) -> None:
        self.__title = title