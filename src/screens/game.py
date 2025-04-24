from pygame import Color
import wsgiref

from core.camera import Camera
from core.screen import Screen
from core.window_data import WindowData
from entities.player import Player
from graphics.widgets.container.container import Container
from graphics.widgets.image.image import Image
from objects.collidable import Collidable


class Game(Screen):


    _player:Player
    _camera:Camera
    _collidables = []

    
    def build(self, windowData:WindowData):
        super().build(windowData)
        
        size = (5, 5)
        tile_pos = (100, 100)
        tile_dimension = (20, 20)
        tile_spacing = (5, 5)
        board = []
        
        for _x in range(0, size[0]):
            for _y in range(0, size[1]):
                _w = tile_dimension[0]
                _h = tile_dimension[1]
                _sX = tile_spacing[0]
                _sY = tile_spacing[1]
                
                board.append(
                    Container(
                        x=tile_pos[0] + _x * _w + _x * _sX,
                        y=tile_pos[1] + _y * _h + _y * _sY,
                        width=_w,
                        height=_h,
                        color=(92, 89, 89)
                    ).onClick(
                        lambda tile: self.change_tile_color(
                            tile, (43, 40, 40)
                        )
                    )
                )
        
        self.addWidget(
            Container(
                width=windowData.getWidth(),
                height=windowData.getHeight(),
                color=(105, 163, 245),
                children=board
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

    
    def change_tile_color(self, tile, color):
        print('changing color')
        tile.color = color

    def update(self):
        pass
        # if not self._isBuilt:
        #     return

        # self._player.tick(
        #     self._collidables
        # )
        # self._camera.tick()