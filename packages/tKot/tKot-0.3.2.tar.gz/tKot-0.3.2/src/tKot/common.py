from dataclasses import dataclass


@dataclass
class Point:
    x: int = 0
    y: int = 0

    @property
    def decoding(self):
        return self.x, self.y

    def move(self, value: int):
        self.x += value
        self.y += value

    def __str__(self):
        return F'<{self.x},{self.y}>'


