import random


class BasePawn:

    def __init__(self) -> None:

        self.id = random.randint(0, 1000)
        self.posx: int = 0
        self.posy: int = 0

    def __str__(self) -> str:
        return f"{self.id} ({self.posx}, {self.posy})"
