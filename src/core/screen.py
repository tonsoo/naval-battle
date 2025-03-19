import abc
import string
from turtle import _Screen

from pygame import Surface

from errors.screens.duplicate_screen_id import DuplicateScreenId


class Screen(abc.ABC):
    
    __id:string
    
    

    @abc.abstractmethod
    def __init__(self, identifier:string=None):

        # verifica se tela com id ja existe
        if not hasattr(Screen, '__list') or Screen.__list is not list:
            Screen.__list = []
        
        if Screen.getScreenById(identifier) != None:
            raise DuplicateScreenId()
        
        # inicializa screen
        super().__init__()
        self.__id = identifier
        
        Screen.__list.append(self)
        
        
        
    def id(self) -> string:
        return self.__id
    
    
    @abc.abstractmethod
    def render(self, surface:Surface):
        pass
    
    
    
    @staticmethod
    def getScreenById(id:string) -> _Screen:
        for screen in Screen.__list:
            if screen.id == id:
                return screen