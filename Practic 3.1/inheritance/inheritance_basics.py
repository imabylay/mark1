"""
inheritance_basics.py

This file demonstrates basic parent and child class relationships.
"""

# Example 1: Basic inheritance
class Person:
    def speak(self):
        print("I am a person.")

class Student(Person):
    pass

student1 = Student()
student1.speak()


# Example 2: Child class adding new method
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog1 = Dog()
dog1.eat()
dog1.bark()


# Example 3: Checking inheritance
print("Example 3:", issubclass(Dog, Animal))


# Example 4: isinstance() check
print("Example 4:", isinstance(dog1, Animal))


# Example 5: Multiple child classes from same parent
class Teacher(Person):
    def teach(self):
        print("Teaching students.")

teacher1 = Teacher()
teacher1.speak()
teacher1.teach()