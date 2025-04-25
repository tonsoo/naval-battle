import pygame
from typing import override
from graphics.widgets.widget import Widget

class ShipWidget(Widget):
    _onDrop = None
    
    def __init__(self, size, horizontal=True, color=(100, 100, 255), x=0, y=0, width=0, height=0):
        self.size = size
        self.horizontal = horizontal
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.color = color
        
        self.onClick(self.click)
        
        super().__init__(x, y, width, height)

        self.last_toggle_time = 0
        self.toggle_timeout = 200

    def setOnDrop(self, callback):
        self._onDrop = callback
        return self


    def toggle_orientation(self):
        self.horizontal = not self.horizontal
        self.width, self.height = self.height, self.width

        self.offset_x = self.height / 2 if self.horizontal else self.width / 2
        self.offset_y = self.height / 2 if self.horizontal else self.width / 2
    
    def click(self, s, event):
        mouse_x, mouse_y = event.pos
        
        if self.dragging:
            self.dragging = False
            if self._onDrop != None:
                self._onDrop(self)
            return
        
        self.dragging = True
        self.offset_x = mouse_x - self.x
        self.offset_y = mouse_y - self.y

    def handleKeys(self, keys):
        current_time = pygame.time.get_ticks()

        if keys[pygame.K_d] and self.dragging:
            if current_time - self.last_toggle_time >= self.toggle_timeout:
                self.toggle_orientation()
                self.last_toggle_time = current_time

    def render(self, surface):
        if self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.x = mouse_x - self.offset_x
            self.y = mouse_y - self.offset_y
            
        pygame.draw.rect(
            surface,
            self.color,
            (self.x, self.y, self.width, self.height)
        )
