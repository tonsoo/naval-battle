from core.screen import Screen
from core.window import Window
from screens.game import Game
from screens.menu.main_menu import MainMenu


class AppWindow(Window):
    
    def __init__(self, app, width = 800, height = 600):
        super().__init__(app, width, height, backgroundColor=(0,0,0))
        
    
    
    def getScreens(self) -> list[Screen]:
        return [MainMenu(), Game()]