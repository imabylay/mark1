"""
method_overriding.py

This file demonstrates method overriding in child classes.
"""

# Example 1: Basic method overriding
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

cat1 = Cat()
cat1.speak()


# Example 2: Overriding with super()
class Bird(Animal):
    def speak(self):
        super().speak()
        print("Chirp")

bird1 = Bird()
bird1.speak()


# Example 3: Overriding return values
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect1 = Rectangle(5, 4)
print("Example 3: Area =", rect1.area())


# Example 4: Overriding with different behavior
class Payment:
    def process(self):
        print("Processing payment")

class CreditCardPayment(Payment):
    def process(self):
        print("Processing credit card payment")

payment = CreditCardPayment()
payment.process()


# Example 5: Demonstrating polymorphism
def make_sound(animal):
    animal.speak()

make_sound(Cat())
make_sound(Bird())