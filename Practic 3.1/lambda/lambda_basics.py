# lambda_basics.py

# This file demonstrates basic usage of lambda functions in Python.
# Lambda functions are small anonymous functions defined using the lambda keyword.
# Syntax: lambda arguments: expression

# Example 1: Simple lambda function
add = lambda a, b: a + b
print("Example 1:", add(5, 3))  # Output: 8


# Example 2: Lambda with one argument
square = lambda x: x * x
print("Example 2:", square(4))  # Output: 16


# Example 3: Lambda with multiple arguments
multiply = lambda x, y, z: x * y * z
print("Example 3:", multiply(2, 3, 4))  # Output: 24


# Example 4: Lambda used immediately (anonymous usage)
print("Example 4:", (lambda x: x + 10)(5))  # Output: 15


# Example 5: Comparing regular function vs lambda

def subtract(a, b):
    return a - b

subtract_lambda = lambda a, b: a - b

print("Example 5 Regular Function:", subtract(10, 3))
print("Example 5 Lambda Function:", subtract_lambda(10, 3))