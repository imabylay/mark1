"""
super_function.py

This file demonstrates usage of super() to call parent methods.
"""

# Example 1: Calling parent constructor
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

student1 = Student("Adil", 95)
print("Example 1:", student1.name, student1.grade)


# Example 2: Calling parent method
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")

dog1 = Dog()
dog1.speak()


# Example 3: Using super() with additional behavior
class Employee:
    def work(self):
        print("Working...")

class Manager(Employee):
    def work(self):
        super().work()
        print("Managing team.")

manager1 = Manager()
manager1.work()


# Example 4: Extending parent attributes
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

car1 = Car("Toyota", "Camry")
print("Example 4:", car1.brand, car1.model)


# Example 5: Multi-level inheritance with super()
class Grandparent:
    def show(self):
        print("Grandparent method")

class Parent(Grandparent):
    def show(self):
        super().show()
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()
        print("Child method")

child1 = Child()
child1.show()