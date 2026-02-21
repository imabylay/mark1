"""
init_method.py

This file demonstrates usage of the __init__() constructor method.
"""

# Example 1: Basic constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Adil", 18)
print("Example 1:", person1.name, person1.age)


# Example 2: Constructor with default value
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

book1 = Book("Python Basics")
print("Example 2:", book1.title, book1.author)


# Example 3: Constructor with calculation
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

rect1 = Rectangle(5, 4)
print("Example 3: Area =", rect1.area)


# Example 4: Multiple objects with constructor
person2 = Person("Anna", 20)
print("Example 4:", person2.name, person2.age)


# Example 5: Constructor validation
class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            balance = 0
        self.balance = balance

account1 = BankAccount(-100)
print("Example 5: Balance =", account1.balance)