import abc
from re import S
import string
from turtle import _Screen

from pygame import Surface

from core.window_data import WindowData
from errors.screens.duplicate_screen_id import DuplicateScreenId
from graphics.widgets.widget import Widget


class Screen(abc.ABC):
    
    __id:string
    __widgets:list[Widget]
    _isBuilt = False
    _windowData:WindowData = None
    

    def __init__(self, identifier:string=None):

        # verifica se tela com id ja existe
        if not hasattr(Screen, '__list') or Screen.__list is not list:
            Screen.__list = []
        
        if Screen.getScreenById(identifier) != None:
            raise DuplicateScreenId()
        
        if identifier == None:
            identifier = str(self.__class__)
        
        # inicializa screen
        super().__init__()
        self.__id = identifier
        self.__widgets = []
        
        Screen.__list.append(self)
        

    @abc.abstractmethod
    def build(self, windowData:WindowData) -> None:
        self._windowData = windowData
        self._isBuilt = True
        
        
    def id(self) -> string:
        return self.__id
    

    def addWidget(self, widget:Widget) -> None:
        self.__widgets.append(widget)
    
    def removeWidget(self, widget:Widget) -> None:
        self.__widgets.remove(widget)
    
    
    def render(self, surface:Surface) -> None:
        for widget in self.__widgets:
            widget.render(surface)

    def handleClick(self, event) -> None:
        for widget in self.__widgets:
            widget.handleClick(event)
            
    def handleKeys(self, keys) -> None:
        for widget in self.__widgets:
            widget.handleKeys(keys)


    def get_widgets(self):
        return self.__widgets
    
    def getWindowData(self):
        return self._windowData



    @abc.abstractmethod
    def update(self) -> None:
        pass
    
    
    
    @staticmethod
    def getScreenById(id:string) -> _Screen:
        for screen in Screen.__list:
            if screen.id() == id:
                return screen