"""
Builder Design Pattern.

Intent: Separate the construction of a complex object from its representation so that the same construction process can
create different representations.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any


class Builder(ABC):

    @abstractmethod
    def set_type(self, t: Type) -> None:
        pass

    @abstractmethod
    def set_seats(self, seats: int) -> None:
        pass

    @abstractmethod
    def set_engine(self, engine: Engine) -> None:
        pass

    @abstractmethod
    def set_transmission(self, transmission: Transmission) -> None:
        pass

    @abstractmethod
    def set_trip_computer(self, trip_computer: TripComputer) -> None:
        pass

    @abstractmethod
    def set_gps_navigator(self, gps_navigator: GPSNavigator) -> None:
        pass


class CarBuilder(Builder):

    def __init__(self) -> None:
        self._type = None
        self._seats = 0
        self._engine = None
        self._transmission = None
        self._trip_computer = None
        self._gps_navigator = None

    def set_type(self, t: Type) -> None:
        self._type = t

    def set_seats(self, seats: int) -> None:
        self._seats = seats

    def set_engine(self, engine: Engine) -> None:
        self._engine = engine

    def set_transmission(self, transmission: Transmission) -> None:
        self._transmission = transmission

    def set_trip_computer(self, trip_computer: TripComputer) -> None:
        self._trip_computer = trip_computer

    def set_gps_navigator(self, gps_navigator: GPSNavigator) -> None:
        self._gps_navigator = gps_navigator

    def build(self):
        return Car(self._type, self._seats, self._engine, self._transmission, self._trip_computer, self._gps_navigator)


class Car:

    def __init__(self, t: Type, seats: int, engine: Engine, transmission: Transmission, trip_computer: TripComputer,
                 gps_navigator: GPSNavigator):
        self._type = t
        self._seats = seats
        self._engine = engine
        self._transmission = transmission
        self._trip_computer = trip_computer
        self._gps_navigator = gps_navigator
        self._fuel = 0.

    def get_type(self):
        return self._type

    def get_seats(self):
        return self._seats

    def get_engine(self):
        return self._engine

    def get_transmission(self):
        return self._transmission

    def get_trip_computer(self):
        return self._trip_computer

    def get_gps_navigator(self):
        return self._gps_navigator

    def get_fuel(self):
        return self._fuel


class Type(Enum):
    CITY_CAR = 1
    SPORTS_CAR = 2
    SUV = 3


class Engine:

    def __init__(self, volume: float, mileage: float):
        self._volume = volume
        self._mileage = mileage
        self._started = False

    def on(self):
        self._started = True

    def off(self):
        self._started = False

    def is_started(self):
        return self._started

    def go(self):
        if self.is_started():
            self._mileage += self._mileage
        else:
            print('Cannot go(), you must start engine first!')

    def get_volume(self):
        return self._volume

    def get_mileage(self):
        return self._mileage


class Transmission(Enum):
    SINGLE_SPEED = 1
    MANUAL = 2
    AUTOMATIC = 3
    SEMI_AUTOMATIC = 4


class GPSNavigator:

    def __init__(self):
        self._route = '221b, Baker Street, London  to Scotland Yard, 8-10 Broadway, London'

    def set_route(self, route):
        self._route = route

    def get_route(self):
        return self._route


class TripComputer:

    def __init__(self):
        self._car = None

    def set_car(self, c: Car):
        self._car = c

    def get_car(self):
        return self._car

    def show_fuel_level(self):
        print('Fuel level: {}'.format(self._car.get_fuel()))

    def show_status(self):
        if self._car.get_engine().is_started():
            print('Car is started')
        else:
            print("Car isn't started")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, b: Builder) -> None:
        self._builder = b

    def build_sport_car(self):
        self._builder.set_type(Type.SPORTS_CAR)
        self._builder.set_seats(2)
        self._builder.set_engine(Engine(3.0, 0))
        self._builder.set_transmission(Transmission.SEMI_AUTOMATIC)
        self._builder.set_trip_computer(TripComputer())
        self._builder.set_gps_navigator(GPSNavigator())

    def build_city_car(self):
        self._builder.set_type(Type.CITY_CAR)
        self._builder.set_seats(2)
        self._builder.set_engine(Engine(1.2, 0))
        self._builder.set_transmission(Transmission.AUTOMATIC)
        self._builder.set_trip_computer(TripComputer())
        self._builder.set_gps_navigator(GPSNavigator())

    def build_suv(self):
        self._builder.set_type(Type.SUV)
        self._builder.set_seats(4)
        self._builder.set_engine(Engine(2.5, 0))
        self._builder.set_transmission(Transmission.MANUAL)
        self._builder.set_gps_navigator(GPSNavigator())


if __name__ == '__main__':
    builder = CarBuilder()

    director = Director()
    director.builder = builder
    director.build_city_car()

    car = builder.build()

    print(car.get_type())
