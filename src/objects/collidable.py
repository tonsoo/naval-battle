from tkinter import Widget


class Collidable:
    
    _widget:Widget
    _can_collide:bool

    def __init__(self, widget, can_collide=False):
        self._widget = widget
        self._can_collide = can_collide
        
    def widget(self):
        return self._widget
    
    def can_collide(self):
        return self._can_collide
    
    def collides(self, rect):
        widgetX = self._widget.x
        widgetWidth = self._widget.width
        widgetY = self._widget.y
        widgetHeight = self._widget.height
        
        targetX = rect.x
        targetY = rect.y
        
        x = targetX > widgetX - widgetWidth / 2 and targetX <= widgetX + widgetWidth / 2
        y = targetY > widgetY - widgetHeight / 2 and targetY <= widgetY + widgetHeight / 2
        
        return x and y