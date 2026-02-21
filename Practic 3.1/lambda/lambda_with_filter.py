# lambda_with_filter.py

# This file demonstrates how to use lambda functions with filter()
# for selecting specific elements from data.


# Example 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Example 1:", even_numbers)


# Example 2: Filter numbers greater than 10
nums = [5, 12, 17, 3, 25]
greater_than_10 = list(filter(lambda x: x > 10, nums))
print("Example 2:", greater_than_10)


# Example 3: Filter words longer than 5 characters
words = ["cat", "elephant", "dog", "giraffe"]
long_words = list(filter(lambda word: len(word) > 5, words))
print("Example 3:", long_words)


# Example 4: Filter positive numbers
mixed_numbers = [-10, 15, -3, 8, 0]
positive_numbers = list(filter(lambda x: x > 0, mixed_numbers))
print("Example 4:", positive_numbers)


# Example 5: Filter students who passed (score >= 60)
students_scores = [45, 78, 90, 55, 62]
passed_students = list(filter(lambda score: score >= 60, students_scores))
print("Example 5:", passed_students)