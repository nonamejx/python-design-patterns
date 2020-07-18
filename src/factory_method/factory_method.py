"""
Factory Method Design Pattern.

Intent: Provide an interface for creating an object, but let subclasses decide which class to instantiate.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def deliver(self) -> str:
        pass


class Truck(Transport):

    def deliver(self) -> str:
        return "Deliver by a Truck"


class Ship(Transport):

    def deliver(self) -> str:
        return "Deliver by a Ship"


class Logistics(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a `Product` class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self) -> None:
        transport = self.create_transport()
        print(f'Create a {transport.__class__.__name__}')
        print(transport.deliver())


class RoadLogistics(Logistics):

    def create_transport(self) -> Truck:
        return Truck()


class SeaLogistics(Logistics):

    def create_transport(self) -> Ship:
        return Ship()


def app(creator: Logistics) -> None:
    """Client code"""
    creator.plan_delivery()


if __name__ == '__main__':
    app(RoadLogistics())
