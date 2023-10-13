import math
from .shape import Shape
# The Circle class also inherits from the Shape class.
# It implements the area() method that returns the area of the circle.
class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius < 0:
            raise ValueError('The radius cannot be negative')
        self._radius = radius

    def area(self) -> float:
        return math.pi * math.pow(self._radius, 2)
