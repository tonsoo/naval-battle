import random
import pygame

from core.screen import Screen
from core.window_data import WindowData
from dev.dev_mode import dprint
from graphics.widgets.container.container import Container
from graphics.widgets.text.text import Text
from objects.game.board import Board
from objects.game.pc_board import PcBoard
from objects.game.placeable_ship import ShipWidget
from objects.game.player_board import PlayerBoard
from objects.game.tiles.ship import Ship


class Game(Screen):

    TURN_COLOR = (7, 171, 37)
    DEFAULT_COLOR = (191, 127, 75)

    _started = False
    _playerBoard = None
    _playerHeader = None
    _pcBoard = None
    _pcHeader = None
    _collidables = []
    _start:int = 0
    _timer:Text = None
    _ship_selection_panel = None
    _ship_tiles = []
    
    board_offset_y = None
    board_offset_x = None
    board_spacing = None
    board_width = None

    
    def build(self, windowData:WindowData):
        super().build(windowData)
        
        self._start = pygame.time.get_ticks()
        self._timer = Text(
            text='-',
            x=windowData.getWidth() / 2 - 100,
            y=0,
            color=(255, 255, 255),
        ).font_size(30)
        
        self.board_offset_y = 80
        self.board_offset_x = 25
        self.board_spacing = 25
        self.board_width = windowData.getWidth() / 2 - self.board_offset_x - self.board_spacing / 2
        
        self.add_boards(windowData)
        
        self.ship_placement(windowData)
        
    def ship_placement(self, windowData):
        board_offset_y = self.board_offset_y
        board_offset_x = self.board_offset_x
        board_spacing = self.board_spacing
        board_width = self.board_width
        
        ships_options = [5, 4, 3, 3, 2]
        cells_hor = self._playerBoard.get_size()[0]
        cells_ver = self._playerBoard.get_size()[1]
        
        panel_width = board_width
        panel_height = windowData.getHeight() - board_offset_y / 2
        ship_spacing = 15
        ship_tile_width = (panel_width) / cells_hor - ship_spacing / cells_hor - self._playerBoard.get_padding()[0] / cells_hor
        ship_tile_height = (panel_height - board_offset_y / 2 - self._playerBoard.get_padding()[1]) / cells_ver - ship_spacing / cells_ver - self._playerBoard.get_padding()[1] / 2

        self._ship_selection_panel = Container(
            x=board_width + board_offset_x + board_spacing,
            y=board_offset_y / 2,
            width=panel_width,
            height=panel_height,
            color=(40, 40, 40),
        )
        self.addWidget(self._ship_selection_panel)
        
        y_offset = 10
        for size in ships_options:
            tile = ShipWidget(
                size=size,
                width=ship_tile_width * size,
                height=ship_tile_height,
                x=board_width + board_offset_x + board_spacing + 10,
                y=board_offset_y / 2 + y_offset,
                color=(100, 100, 255)
            ).setOnDrop(self.snap_to_board)
            
            self._ship_tiles.append(tile)
            self.addWidget(tile)
            
            y_offset += ship_tile_width + ship_spacing


    def snap_to_board(self, ship: ShipWidget):
        board = self._playerBoard
        
        mx, my = pygame.mouse.get_pos()
        
        tile = board.find_nearest_tile(mx, my)
        if tile is None:
            return
        
        tile_x, tile_y = tile
        snapped_x, snapped_y = board.grid_to_screen(tile_x, tile_y)
        ship.x = snapped_x
        ship.y = snapped_y


    def start_game(self):
        self._started = True
        
        if random.randint(0, 100) > 50:
            self._playerBoard.give_turn()
            dprint('player turn')
            
            self.next_turn()
        else:
            self._pcBoard.give_turn()
            dprint('pc turn')
            
    def validate_and_place_ships(self):
        board = self._playerBoard

        occupied = set()
        ships = []

        for widget in self.get_widgets():
            if isinstance(widget, ShipWidget) and not widget.dragging:
                center_x = widget.x
                center_y = widget.y

                start_tile = board.find_nearest_tile(center_x, center_y)
                if not start_tile:
                    self._timer.text('Posicione os navios')
                    return False

                start_x, start_y = start_tile

                for i in range(widget.size):
                    tile_x = start_x + i if widget.horizontal else start_x
                    tile_y = start_y if widget.horizontal else start_y + i

                    if tile_x >= board.get_size()[0] or tile_y >= board.get_size()[1]:
                        self._timer.text('Navios fora do tabuleiro')
                        return False

                    if (tile_x, tile_y) in occupied:
                        self._timer.text('Navios em sobreposição')
                        return False

                    occupied.add((tile_x, tile_y))

                ships.append({
                    "start": (start_x, start_y),
                    "horizontal": widget.horizontal,
                    "size": widget.size,
                    "tiles": [ (start_x + i if widget.horizontal else start_x,
                                start_y if widget.horizontal else start_y + i)
                            for i in range(widget.size) ]
                })

        if len(ships) < 5:
            print("Not all ships placed")
            return False

        for ship in ships:
            board.place_ship(
                x=ship["start"][0],
                y=ship["start"][1],
                vertical=not ship["horizontal"],
                length=ship["size"]
            )
        print("All ships validated and placed!")
        
        self._playerBoard.generate_board_with_bombs()
        
        self.removeWidget(self._ship_selection_panel)
        for ship_tile in self._ship_tiles:
            self.removeWidget(ship_tile)
        self._ship_tiles = []
        
        self.start_game()
        
        return True



    def add_boards(self, windowData):
        board_offset_y = self.board_offset_y
        board_offset_x = self.board_offset_x
        board_spacing = self.board_spacing
        board_width = self.board_width
        
        self._playerBoard = PlayerBoard(
            game=self,
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
        
        self._pcBoard = PcBoard(
            game=self,
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
        
        if self._timer == None or not self._started:
            return
        
        elapsed_time = pygame.time.get_ticks() - self._start
        seconds = elapsed_time // 1000
        minutes = seconds // 60
        seconds = seconds % 60

        txt = f'Tempo: {minutes:02}:{seconds:02}'
        self._timer.text(txt)
        
    def next_turn(self):
        if self._playerBoard.has_turn():
            tile = None
            while tile == None:
                position_index = random.randint(0, self._playerBoard.remaining.__len__() - 1)
                position = self._playerBoard.remaining[position_index]
                
                tile = self._playerBoard.get_tile_at(
                    position[0],
                    position[1]
                )
                
                if tile.is_open():
                    self._playerBoard.remaining.remove(tile.get_index())
                    tile = None
                
            self._playerBoard.attack_tile(tile, None)
            self._playerBoard.remaining.remove(tile.get_index())

            if not isinstance(tile, Ship):
                self._playerBoard.take_turn()
                self._pcBoard.give_turn()
            else:
                self.next_turn()
        elif self._pcBoard.has_turn():
            self._pcBoard.take_turn()
            self._playerBoard.give_turn()
            self.next_turn()
        
    def handleKeys(self, keys):
        super().handleKeys(keys)

        if keys[pygame.K_RETURN]:
            self.validate_and_place_ships()