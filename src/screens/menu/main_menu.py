import string

from core.screen import Screen
from entities.player import Player


class MainMenu(Screen):


    _player:Player

    
    def __init__(self, identifier:string = None):
        super().__init__(identifier)

        self._player = Player(speed=120, sprintSpeed=200)
        self.addWidget(self._player)

    

    def update(self):
        self._player.tick()