# class_definition.py
# This file demonstrates basic class definition and object creation in Python.


# Example 1: Simple class with attributes
class Person:
    name = "Unknown"
    age = 0

person1 = Person()
print("Example 1:", person1.name, person1.age)


# Example 2: Creating multiple objects
person2 = Person()
person2.name = "Adil"
person2.age = 18
print("Example 2:", person2.name, person2.age)


# Example 3: Adding a method inside class
class Car:
    brand = "Toyota"

    def drive(self):
        print("The car is driving.")

car1 = Car()
print("Example 3:", car1.brand)
car1.drive()


# Example 4: Accessing object properties
class Student:
    university = "AITU"

student1 = Student()
print("Example 4:", student1.university)


# Example 5: Creating class with pass statement
class EmptyClass:
    pass

empty_object = EmptyClass()
print("Example 5: Empty class object created successfully.")