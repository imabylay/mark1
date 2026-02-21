"""
class_variables.py

This file demonstrates class variables vs instance variables.
"""

# Example 1: Class variable shared by all objects
class School:
    school_name = "International School"

student1 = School()
student2 = School()

print("Example 1:", student1.school_name)
print("Example 1:", student2.school_name)


# Example 2: Changing class variable affects all objects
School.school_name = "AITU"
print("Example 2:", student1.school_name)
print("Example 2:", student2.school_name)


# Example 3: Instance variable overriding class variable
class Person:
    species = "Human"

person1 = Person()
person1.species = "Cyborg"

print("Example 3 Person1:", person1.species)
print("Example 3 Class:", Person.species)


# Example 4: Counting objects using class variable
class Employee:
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

e1 = Employee("Adil")
e2 = Employee("Anna")

print("Example 4: Total employees =", Employee.employee_count)


# Example 5: Deleting object property
class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("BMW")
print("Example 5 Before delete:", car1.brand)

del car1.brand
print("Example 5: brand property deleted.")