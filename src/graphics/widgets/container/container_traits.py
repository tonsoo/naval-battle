from enum import Enum


class ContainerTraits(Enum):

    WIDTH_FULL = 'container.trait.width.full'
    HEIGHT_FULL = 'container.trait.height.full'

    WIDTH_AUTO = 'container.trait.width.auto'
    HEIGHT_AUTO = 'container.trait.height.auto'

    HORIZONTAL_LEFT = 'container.trait.alignment.horizontal.left'
    HORIZONTAL_CENTER = 'container.trait.alignment.horizontal.center'
    HORIZONTAL_RIGHT = 'container.trait.alignment.horizontal.right'

    VERTICAL_LEFT = 'container.trait.alignment.vertical.left'
    VERTICAL_CENTER = 'container.trait.alignment.vertical.center'
    VERTICAL_RIGHT = 'container.trait.alignment.vertical.right'