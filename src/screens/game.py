from pygame import Color
import wsgiref

from core.camera import Camera
from core.screen import Screen
from core.window_data import WindowData
from entities.player import Player
from graphics.widgets.container.container import Container
from graphics.widgets.image.image import Image
from objects.collidable import Collidable
from objects.game.board import Board
from objects.game.tile import Tile


class Game(Screen):


    _player:Player
    _camera:Camera
    _collidables = []

    
    def build(self, windowData:WindowData):
        super().build(windowData)
        
        self.addWidget(
            Board(
                size=(11, 9),
                padding=(10, 20),
                spacing=(8, 10),
                ships=3,
                width=windowData.getWidth(),
                height=windowData.getHeight(),
            )
        )

    def _tile_index(self, width, x, y):
        return x + y * width

    def update(self):
        pass