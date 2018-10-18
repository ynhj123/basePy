from Test1.Ball import Ball


class Player(Ball):
    def __init__(self, position, radius) -> None:
        super().__init__(position, radius)