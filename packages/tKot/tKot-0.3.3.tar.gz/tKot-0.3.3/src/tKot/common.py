from dataclasses import dataclass
from typing import Self


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

    def __mul__(self, other: int | float) -> Self:
        """:return Point with scaler x and y by other value"""
        if isinstance(other, (int, float)):
            self.x = self.x*other
            self.y = self.y*other
            return self
        else:
            ValueError(F"got unsupport type: {other}, expected int or float")
