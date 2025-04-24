import pygame

from core.camera import Camera
from core.screen import Screen
from core.window_data import WindowData
from dev.dev_mode import dprint
from entities.player import Player
from graphics.widgets.container.container import Container
from graphics.widgets.text.text import Text
from objects.game.board import Board
from objects.game.player_board import PlayerBoard


class Game(Screen):


    _player:Player
    _camera:Camera
    _collidables = []
    _start:int = 0
    _timer:Text = None

    
    def build(self, windowData:WindowData):
        super().build(windowData)
        
        self._start = pygame.time.get_ticks()
        self._timer = Text(
            text='-',
            x=windowData.getWidth() / 2 - 100,
            y=0,
            color=(255, 255, 255),
        ).font_size(30)
        
        board_offset_y = 80
        board_offset_x = 25
        board_spacing = 25
        board_width = windowData.getWidth() / 2 - board_offset_x - board_spacing / 2
        self.addWidget(
            Container(
                width=windowData.getWidth(),
                height=windowData.getHeight(),
                color=(11, 40, 94),
                children=[
                    Container(
                        width=board_width,
                        height=board_offset_y - 45,
                        y=45,
                        color=(105, 131, 245),
                        x=board_offset_x
                    ),
                    Text(
                        text='Player',
                        color=(255, 255, 255),
                        x=150 + board_offset_x,
                        y=50,
                    ).font_size(20),
                    PlayerBoard(
                        size=(9, 15),
                        padding=(10, 20),
                        spacing=(8, 10),
                        ships=3,
                        ships_sizes=[[2, 5], [3, 3], [4, 2], [5, 1], [6, 1]],
                        width=board_width,
                        height=windowData.getHeight() - board_offset_y,
                        y=board_offset_y,
                        x=board_offset_x
                    ),
                    
                    Container(
                        width=board_width,
                        height=board_offset_y - 45,
                        y=45,
                        color=(105, 131, 245),
                        x=board_width + board_offset_x + board_spacing,
                    ),
                    Text(
                        text='PC',
                        color=(255, 255, 255),
                        x=board_width + 170 + board_offset_x + board_spacing,
                        y=50,
                    ).font_size(20),
                    Board(
                        size=(9, 15),
                        padding=(10, 20),
                        spacing=(8, 10),
                        ships=3,
                        ships_sizes=[[2, 5], [3, 3], [4, 2], [5, 1], [6, 1]],
                        width=board_width,
                        height=windowData.getHeight() - board_offset_y,
                        y=board_offset_y,
                        x=board_width + board_offset_x + board_spacing,
                    ),
                    self._timer
                ]
            )
        )

    def _tile_index(self, width, x, y):
        return x + y * width

    def update(self):
        if self._timer == None:
            return
        
        elapsed_time = pygame.time.get_ticks() - self._start
        seconds = elapsed_time // 1000
        minutes = seconds // 60
        seconds = seconds % 60

        txt = f'Tempo: {minutes:02}:{seconds:02}'
        dprint(txt)
        self._timer.text(txt)