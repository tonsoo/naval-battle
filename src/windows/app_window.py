from turtle import Screen
from core.window import Window
from screens.menu import main_menu


class AppWindow(Window):
    
    def __init__(self, width = 800, height = 600):
        super().__init__(width, height)
        
    
    
    def getScreens(self) -> list[Screen]:
        return [main_menu]