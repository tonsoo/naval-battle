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
                width=windowData.getWidth(),
                height=windowData.getHeight(),
            )
        )
        
        # self._camera = Camera(windowData, 0, 0)
        # self._player = Player(speed=120, sprintSpeed=360)

        # self._camera.watch(self._player)
        
        # self._collidables = [
        #     Collidable(
        #         Container(0, 0, 20, 20, Color(255, 0, 0))
        #     ),
        #     Collidable(
        #         Container(300, 122, 100, 100, Color(0, 255, 0))
        #     ),
        #     Collidable(
        #         Image('assets/icons/close_1.png', x=300, y=122, width=100, height=100),
        #         can_collide=True
        #     )
        # ]
        
        # for c in self._collidables:
        #     self._camera.addChild(c.widget())
            
        # self._camera.addChild(self._player)
        # self.addWidget(self._camera)

    def _tile_index(self, width, x, y):
        return x + y * width

    def update(self):
        pass
        # if not self._isBuilt:
        #     return

        # self._player.tick(
        #     self._collidables
        # )
        # self._camera.tick()