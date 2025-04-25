import pygame
from graphics.widgets.widget import Widget

class ShipWidget(Widget):
    def __init__(self, size, horizontal=True, color=(100, 100, 255), x=0, y=0, width=0, height=0):
        self.size = size
        self.horizontal = horizontal
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.color = color
        
        self.onClick(self.click)
        
        super().__init__(x, y, width, height)

    def toggle_orientation(self):
        self.horizontal = not self.horizontal
        self.width, self.height = self.height, self.width
    
    def click(self, s, event):
        mouse_x, mouse_y = event.pos
        
        if self.dragging:
            self.dragging = False
            return
        
        self.dragging = True
        self.offset_x = mouse_x - self.x
        self.offset_y = mouse_y - self.y

    def handleKeys(self, keys):
        print('?')
        if keys[pygame.K_d] and self.dragging:
            self.toggle_orientation()

    def render(self, surface):
        if self.dragging:
            print('updating dragging element')
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.x = mouse_x - self.offset_x
            self.y = mouse_y - self.offset_y
            
        pygame.draw.rect(
            surface,
            self.color,
            (self.x, self.y, self.width, self.height)
        )
