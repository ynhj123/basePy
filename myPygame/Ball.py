import time

from myPygame.Contants import SPEED


class Ball:
    def __init__(self, position, radius) -> None:
        self.postition = position
        self.radius = radius

    def move_x(self, x):
        self.postition.x += x

    def move_y(self, y):
        self.postition.y += y

    def move_to(self, postition):
        self.postition = postition

    def move_x_speed(self, x, speed):
        if (self.postition.x <= x):
            while self.postition.x >= x:
                time.sleep(SPEED)
                self.postition.x += speed
        else:
            while self.postition.x <= x:
                time.sleep(SPEED)
                self.postition.x -= speed

    def move_y_speed(self, y, speed):
        if (self.postition.y <= y):
            while self.postition.y >= y:
                time.sleep(SPEED)
                self.postition.y += speed
        else:
            while self.postition.y <= y:
                time.sleep(SPEED)
                self.postition.y -= speed


