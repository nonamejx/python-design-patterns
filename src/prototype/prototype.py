"""
Prototype Design Pattern.

Intent: Specify the kinds of objects to create using a prototypical instance, and create new objects by copying
this prototype.

Python provides its own interface of Prototype via `copy.copy` and `copy.deepcopy` functions.
Custom implementations could be done via overriding `__copy__` and `__deepcopy__` member functions.
"""
from __future__ import annotations

import copy
from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @abstractmethod
    def clone(self):
        pass


class Circle(Shape):

    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y)
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)


class Rectangle(Shape):

    def __init__(self, x: float, y: float, width: float, height: float):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    circle = Circle(1, 2, 3)
    another_circle = circle.clone()
    print(f'id-{circle} - value-{circle.__dict__}')
    print(f'id-{another_circle} - value-{another_circle.__dict__}')
