from typing import Text
from core.screen import Screen
from core.window_data import WindowData
from graphics.widgets.container.container import Container
from graphics.widgets.container.container_traits import ContainerTraits
from graphics.widgets.padding.edge_insets import EdgeInsets
from graphics.widgets.padding.padding import Padding
from graphics.widgets.text import text


class MainMenu(Screen):

    
    def build(self, windowData:WindowData):
        super().__init__(windowData)
        
        self.addWidget(
            Container(
                width=windowData.getWidth(),
                height=windowData.getHeight(),
                color=(212, 212, 212),
                children=[
                    Container(
                        width=200,
                        height=50,
                        color=(223, 123, 175),
                        children=[
                            text.Text('alo')
                        ]
                    )
                ]
            )
        )



    def update(self):
        pass