"""
lambda_with_map.py

This file demonstrates how to use lambda functions with map()
for transforming data.
"""

# Example 1: Square numbers in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Example 1:", squared)


# Example 2: Convert temperatures from Celsius to Fahrenheit
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Example 2:", fahrenheit)


# Example 3: Convert names to uppercase
names = ["adil", "python", "lambda"]
uppercase_names = list(map(lambda name: name.upper(), names))
print("Example 3:", uppercase_names)


# Example 4: Calculate lengths of words
words = ["apple", "banana", "cherry"]
lengths = list(map(lambda word: len(word), words))
print("Example 4:", lengths)


# Example 5: Add two lists element-wise
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_lists = list(map(lambda x, y: x + y, list1, list2))
print("Example 5:", sum_lists)