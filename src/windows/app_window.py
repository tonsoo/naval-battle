from core.screen import Screen
from core.window import Window
from screens.menu.main_menu import MainMenu


class AppWindow(Window):
    
    def __init__(self, width = 800, height = 600):
        super().__init__(width, height)
        
    
    
    def getScreens(self) -> list[Screen]:
        return [MainMenu(self)]