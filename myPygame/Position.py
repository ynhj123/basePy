class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


    def __eq__(self, position):
        return self.x == position.x and self.y == position.y
