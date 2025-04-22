import pygame
from core.time import Time
from entities.entity import Entity


class Player(Entity):
    
    __sprintSpeed:float
    __keyMap:dict = {
        'left': [pygame.K_LEFT, pygame.K_a],
        'right': [pygame.K_RIGHT, pygame.K_d],
        'up': [pygame.K_UP, pygame.K_w],
        'down': [pygame.K_DOWN, pygame.K_s],
        'sprint': [pygame.K_LSHIFT, pygame.K_RSHIFT],
    }
    _color = (89, 67, 234)
    _sprintColor = (169, 67, 187)
    _renderColor:pygame.Color
    
    def __init__(self, x=0, y=0, width=15, height=25, speed=100, sprintSpeed:float=150):
        super().__init__(x, y, width, height, speed)
        self.__sprintSpeed = sprintSpeed
        self._renderColor = self._color
        
        
    
    def tick(self):
        self.move()
    
    def render(self, surface):
        pygame.draw.rect(
            surface,
            color=self._renderColor,
            rect=[self.x, self.y, self.width, self.height]
        )
        
        
        
    def move(self):
        x = 0
        y = 0
        speed = self._speed
        
        keys=pygame.key.get_pressed()
        if self._hasKeyPressed(self.__keyMap['left'], keys):
            x = -1
        elif self._hasKeyPressed(self.__keyMap['right'], keys):
            x = 1

        if self._hasKeyPressed(self.__keyMap['up'], keys):
            y = -1
        elif self._hasKeyPressed(self.__keyMap['down'], keys):
            y = 1
            
        if self._hasKeyPressed(self.__keyMap['sprint'], keys):
            speed = self.__sprintSpeed
            self._renderColor = self._sprintColor
        else:
            self._renderColor = self._color
            
        self.x = self.x + x * speed * Time.deltaTime()
        self.y = self.y + y * speed * Time.deltaTime()
        
    def _hasKeyPressed(self, keyList:list[int], keys:dict) -> bool:
        for key in keyList:
            if keys[key]:
                return True
            
        return False