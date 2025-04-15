import re
from graphics.widgets.container.container import Container
from graphics.widgets.padding.edge_insets import EdgeInsets
from models.generics.rect import Rect


class Padding(Container):

    __padding:EdgeInsets


    def __init__(self, x=0, y=0, width=0, height=0, color = (0,0,0), children = [], padding:EdgeInsets = EdgeInsets.zero()):
        super().__init__(x, y, width, height, color, children)

        self.__padding = padding

    def renderIndividualChild(self, surface, child):
        rect = Rect(
            x=child.x, y=child.y,
            width=child.width, height=child.height
        )

        child.x = child.x + self.__padding.left
        child.width = child.width - self.__padding.left - self.__padding.right

        child.y = child.y + self.__padding.top
        child.height = child.height - self.__padding.top - self.__padding.bottom
        
        super().renderIndividualChild(surface, child)

        child.x = rect.x
        child.y = rect.y

        child.width = rect.width
        child.height = rect.height