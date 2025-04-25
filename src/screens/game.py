import random
import pygame

from core.screen import Screen
from core.window_data import WindowData
from dev.dev_mode import dprint
from graphics.widgets.container.container import Container
from graphics.widgets.text.text import Text
from objects.game.board import Board
from objects.game.placeable_ship import ShipWidget
from objects.game.player_board import PlayerBoard


class Game(Screen):

    TURN_COLOR = (7, 171, 37)
    DEFAULT_COLOR = (191, 127, 75)

    _playerBoard = None
    _playerHeader = None
    _pcBoard = None
    _pcHeader = None
    _collidables = []
    _start:int = 0
    _timer:Text = None
    _ship_selection_panel = None

    
    def build(self, windowData:WindowData):
        super().build(windowData)
        
        self._start = pygame.time.get_ticks()
        self._timer = Text(
            text='-',
            x=windowData.getWidth() / 2 - 100,
            y=0,
            color=(255, 255, 255),
        ).font_size(30)
        
        self.add_boards(windowData)
        
        self.ship_placement()
        
    def ship_placement(self):
        ship_list = []

        ships_options = [5, 4, 3, 3, 2]
        largest = max(ships_options)
        
        panel_width = 150
        ship_spacing = 15
        ship_tile_size = panel_width / largest - ship_spacing / largest
        
        y_offset = 10
        for size in ships_options:
            ship_list.append(
                ShipWidget(
                    size=size,
                    width=ship_tile_size * size,
                    height=ship_tile_size,
                    x=10,
                    y=y_offset,
                    color=(100, 100, 255)
                )
            )
            y_offset += ship_tile_size + ship_spacing
        
        self._ship_selection_panel = Container(
            x=10,
            y=10,
            width=panel_width,
            height=500,
            color=(40, 40, 40),
            children=ship_list
        )
        self.addWidget(self._ship_selection_panel)

    def add_boards(self, windowData):
        board_offset_y = 80
        board_offset_x = 25
        board_spacing = 25
        board_width = windowData.getWidth() / 2 - board_offset_x - board_spacing / 2

        self._playerBoard = PlayerBoard(
            size=(9, 15),
            padding=(10, 20),
            spacing=(8, 10),
            ships=3,
            ships_sizes=[[2, 5], [3, 3], [4, 2], [5, 1], [6, 1]],
            width=board_width,
            height=windowData.getHeight() - board_offset_y,
            y=board_offset_y,
            x=board_offset_x
        )
        
        self._playerHeader = Container(
            width=board_width,
            height=board_offset_y - 45,
            y=45,
            color=(105, 131, 245),
            x=board_offset_x
        )
        
        self._pcBoard = Board(
            size=(9, 15),
            padding=(10, 20),
            spacing=(8, 10),
            ships=3,
            ships_sizes=[[2, 5], [3, 3], [4, 2], [5, 1], [6, 1]],
            width=board_width,
            height=windowData.getHeight() - board_offset_y,
            y=board_offset_y,
            x=board_width + board_offset_x + board_spacing,
        )
        
        self._pcHeader = Container(
            width=board_width,
            height=board_offset_y - 45,
            y=45,
            color=(105, 131, 245),
            x=board_width + board_offset_x + board_spacing,
        )
        
        if random.randint(0, 100) > 50:
            self._playerBoard.give_turn()
            dprint('player turn')
        else:
            self._pcBoard.give_turn()
            dprint('pc turn')
        
        self.addWidget(
            Container(
                width=windowData.getWidth(),
                height=windowData.getHeight(),
                color=(11, 40, 94),
                children=[
                    self._playerHeader,
                    Text(
                        text='Player',
                        color=(255, 255, 255),
                        x=150 + board_offset_x,
                        y=50,
                    ).font_size(20),
                    self._playerBoard,
                    
                    self._pcHeader,
                    Text(
                        text='PC',
                        color=(255, 255, 255),
                        x=board_width + 170 + board_offset_x + board_spacing,
                        y=50,
                    ).font_size(20),
                    self._pcBoard,
                    self._timer
                ]
            )
        )

    def _tile_index(self, width, x, y):
        return x + y * width

    def update_boards(self):
        if self._playerBoard != None:
            self._playerBoard.refresh_tiles()
            self._playerHeader.color = self.TURN_COLOR if self._playerBoard.has_turn() else self.DEFAULT_COLOR

        if self._pcBoard != None:
            self._pcBoard.refresh_tiles()
            self._pcHeader.color = self.TURN_COLOR if self._pcBoard.has_turn() else self.DEFAULT_COLOR
        
    def update(self):
        self.update_boards()
        
        if self._timer == None:
            return
        
        elapsed_time = pygame.time.get_ticks() - self._start
        seconds = elapsed_time // 1000
        minutes = seconds // 60
        seconds = seconds % 60

        txt = f'Tempo: {minutes:02}:{seconds:02}'
        self._timer.text(txt)