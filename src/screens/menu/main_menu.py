from typing import Text

from pygame import Color
import pygame
from core.screen import Screen
from core.window_data import WindowData
from graphics.widgets.container.container import Container
from graphics.widgets.container.container_traits import ContainerTraits
from graphics.widgets.padding.edge_insets import EdgeInsets
from graphics.widgets.padding.padding import Padding
from graphics.widgets.text import text


class MainMenu(Screen):

    
    def build(self, windowData:WindowData):
        super().build(windowData)
        
        self.addWidget(
            Container(
                width=windowData.getWidth(),
                height=windowData.getHeight(),
                color=(105, 163, 245),
                children=[
                    Container(
                        width=200,
                        height=50,
                        x=windowData.getWidth() / 2 - 100,
                        y=windowData.getHeight() / 2,
                        color=(70, 123, 205),
                        children=[
                            text.Text('JOGAR',
                                    x=50,
                                    y=5,
                                )
                                .font_size(30)
                        ]
                    ).onClick(lambda: windowData.getApp().get_window().changeScreen(1)),
                    Container(
                        width=200,
                        height=50,
                        x=windowData.getWidth() / 2 - 100,
                        y=windowData.getHeight() / 2 + 60,
                        color=(70, 123, 205),
                        children=[
                            text.Text('SAIR',
                                    x=70,
                                    y=5,
                                )
                                .font_size(30)
                        ]
                    ).onClick(lambda: pygame.quit())
                ]
            )
        )



    def update(self):
        if not self._isBuilt:
            return
        pass