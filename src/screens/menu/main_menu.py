from core.screen import Screen
from core.window_data import WindowData
from graphics.widgets.container.container import Container
from graphics.widgets.container.container_traits import ContainerTraits
from graphics.widgets.padding.edge_insets import EdgeInsets
from graphics.widgets.padding.padding import Padding


class MainMenu(Screen):

    
    def build(self, windowData:WindowData):
        super().__init__(windowData)
        
        self.addWidget(
            Container(
                width=windowData.getWidth(),
                height=windowData.getHeight(),
                color=(212, 212, 212),
                children=[
                    Padding(
                        width=ContainerTraits.WIDTH_FULL,
                        padding=EdgeInsets.symetrical(
                            vertical=20,
                            horizontal=10
                        ),
                        children=[
                            Container(
                                width=ContainerTraits.WIDTH_FULL,
                                height=50,
                                color=(122, 12, 10)
                            )
                        ]
                    )
                ]
            )
        )



    def update(self):
        pass