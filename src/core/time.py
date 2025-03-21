import pygame


class Time:
    
    _deltaTime:float = 0
    _clock = pygame.time.Clock()
    
    
    
    @staticmethod
    def deltaTime() -> float:
        return Time._deltaTime
    
    
    
    @staticmethod
    def update() -> None:
        Time._deltaTime = Time._clock.tick(60) / 1000.0