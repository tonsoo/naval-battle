from pygame import Color

from core.camera import Camera
from core.screen import Screen
from core.window_data import WindowData
from entities.player import Player
from graphics.widgets.container.container import Container
from graphics.widgets.image.image import Image


class Game(Screen):


    _player:Player
    _camera:Camera

    
    def build(self, windowData:WindowData):
        super().build(windowData)
        
        self._camera = Camera(windowData, 0, 0)
        self._player = Player(speed=120, sprintSpeed=360)

        self._camera.watch(self._player)
        self._camera.addChild(Container(0, 0, 20, 20, Color(255, 0, 0)))
        self._camera.addChild(
            Image('assets/icons/close_1.png', x=300, y=122, width=100, height=100)
        )
        self._camera.addChild(self._player)
        self.addWidget(self._camera)

    

    def update(self):
        if not self._isBuilt:
            return

        self._player.tick()
        self._camera.tick()