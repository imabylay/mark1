"""
class_methods.py

This file demonstrates instance methods and the self parameter.
"""

# Example 1: Simple instance method
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Woof!")

dog1 = Dog("Buddy")
dog1.bark()


# Example 2: Method using object attributes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

circle1 = Circle(5)
print("Example 2: Area =", circle1.calculate_area())


# Example 3: Modifying object property inside method
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

counter = Counter()
counter.increment()
print("Example 3: Count =", counter.count)


# Example 4: Method calling another method
class Greeting:
    def say_hello(self):
        print("Hello!")

    def greet(self):
        self.say_hello()
        print("Welcome!")

g = Greeting()
g.greet()


# Example 5: Method returning formatted string
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_info(self):
        return f"{self.name} has grade {self.grade}"

student1 = Student("Adil", 95)
print("Example 5:", student1.get_info())