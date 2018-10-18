
class Ball:
    def __init__(self, position, radius) -> None:
        self.postition = position
        self.radius = radius

    def move_x(self, x):
        self.postition.x += x

    def move_y(self, y):
        self.postition.y += y


