class EdgeInsets:
    left:float
    right:float
    top:float
    bottom:float


    def __init__(self, top:float = 0, right:float = 0, bottom:float = 0, left:float = 0):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def symetrical(vertical:float = 0, horizontal:float = 0):
        return EdgeInsets(
            top=vertical, bottom=vertical,
            left=horizontal, right=horizontal
        )
    
    def all(padding:float = 0):
        return EdgeInsets(
            top=padding, bottom=padding,
            left=padding, right=padding
        )
    
    def zero():
        return EdgeInsets.all(0)