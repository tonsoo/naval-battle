from platform import win32_edition
from pygame import Surface
from core.time import Time
from core.window import Window
from graphics.widgets.widget import Widget
from models.generics.rect import Rect


class Camera(Widget):

    _children:list[Widget]
    _watch:Widget
    _offsetX:float
    _offsetY:float
    _moveX:float
    _moveY:float
    _window:Window

    
    def __init__(self, window:Window, x = 0, y = 0, offsetX = 25, offsetY = 15, moveX = 3, moveY = 3):
        super().__init__(x, y)

        self._window = window
        self._watch = None

        self._children = []

        self._offsetX = offsetX
        self._offsetY = offsetY

        self._moveX = moveX
        self._moveY = moveY

    def watch(self, rect:Widget) -> None:
        self._watch = rect

    def addChild(self, child:Widget) -> None:
        self._children.append(child)
    

    def render(self, surface:Surface):
        for child in self._children:
            self.renderChild(surface, child)

    def renderChild(self, surface:Surface, child:Widget,) -> None:
        [tmpX, tmpY] = [child.x, child.y]
        child.x = child.x - child.width / 2 - self.x + self._window.getWidth() / 2
        child.y = child.y - child.height / 2 - self.y + self._window.getHeight() / 2

        child.render(surface)

        child.x = tmpX
        child.y = tmpY

    def tick(self) -> None:
        self.x = self.x + self.calculateMovement(self._watch.x, self.x, self._offsetX, self._moveX) * Time.deltaTime()
        self.y = self.y + self.calculateMovement(self._watch.y, self.y, self._offsetY, self._moveY) * Time.deltaTime()

    def calculateMovement(self, pos1:float, pos2:float, minOffset:float, speed:float) -> float:
        composite = pos1 - pos2
        move = 0
        if composite > minOffset:
            move = abs(composite) - abs(minOffset)
        elif composite < -minOffset:
            move = (abs(composite) - abs(minOffset)) * -1
        return move * speed

    def isOutsideX(self) -> bool:
        return self._watch.x < self.x or self._watch.x - self._watch.width > self.x + self._window.getWidth()
    
    def isOutsideY(self) -> bool:
        return self._watch.y < self.y or self._watch.y - self._watch.height > self.y + self._window.getHeight()