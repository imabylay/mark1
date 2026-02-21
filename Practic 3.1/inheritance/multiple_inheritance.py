"""
multiple_inheritance.py

This file demonstrates multiple inheritance and abstract base classes.
"""

from abc import ABC, abstractmethod

# Example 1: Basic multiple inheritance
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()


# Example 2: Method Resolution Order (MRO)
print("Example 2 MRO:", Duck.__mro__)


# Example 3: Conflict resolution
class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    pass

c1 = C()
c1.show()  # Follows MRO


# Example 4: Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle1 = Circle(5)
print("Example 4: Circle area =", circle1.area())


# Example 5: Another abstract example
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

car1 = Car()
car1.start()