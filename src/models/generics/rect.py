from models.generics.position import Position


class Rect(Position):
    width:float
    height:float


    def __init__(self, x:float = 0, y:float = 0, width:float = 0, height:float = 0):
        super().__init__(x, y)

        self.width = width
        self.height = height