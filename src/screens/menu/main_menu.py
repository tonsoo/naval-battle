import string

from pygame import Color

from core.camera import Camera
from core.screen import Screen
from entities.player import Player
from graphics.widgets.container import Container


class MainMenu(Screen):


    _player:Player
    _camera:Camera

    
    def __init__(self, window, identifier:string = None):
        super().__init__(window, identifier)

        self._camera = Camera(self._window, 0, 0)
        self._player = Player(speed=120, sprintSpeed=200)

        self._camera.watch(self._player)
        self._camera.addChild(Container(0, 0, 20, 20, Color(255, 0, 0)))
        self._camera.addChild(self._player)
        self.addWidget(self._camera)

    

    def update(self):
        self._player.tick()
        self._camera.tick()