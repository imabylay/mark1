# lambda_with_sorted.py

# This file demonstrates how to use lambda functions with sorted()
# for custom sorting.


# Example 1: Sort numbers by absolute value
numbers = [-10, 5, -3, 8, -2]
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))
print("Example 1:", sorted_by_abs)


# Example 2: Sort words by length
words = ["apple", "kiwi", "banana", "cherry"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print("Example 2:", sorted_by_length)


# Example 3: Sort list of tuples by second value
pairs = [(1, 3), (4, 1), (2, 2)]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print("Example 3:", sorted_pairs)


# Example 4: Sort students by grade
students = [
    {"name": "Adil", "grade": 85},
    {"name": "Anna", "grade": 92},
    {"name": "John", "grade": 78}
]

sorted_students = sorted(students, key=lambda student: student["grade"])
print("Example 4:", sorted_students)


# Example 5: Sort by multiple criteria (age, then name)
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 25}
]

sorted_people = sorted(people, key=lambda person: (person["age"], person["name"]))
print("Example 5:", sorted_people)