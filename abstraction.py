# Day 13 - Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

class Bike(Vehicle):

    def start(self):
        print("Bike Started")

Car().start()
Bike().start()