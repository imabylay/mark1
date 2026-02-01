# Introduction to Booleans in Python

# Example 1: Basic boolean comparisons
print(10 > 9)
print(10 == 9)
print(10 < 9)


# 2: Boolean values in if statement
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")



#3: Using bool() with values
print(bool("Hello"))
print(bool(15))
print(bool(""))



# 4: Using bool() with variables
x = "Python"
y = 0

print(bool(x))
print(bool(y))



# 5: Function returning a boolean
def my_function():
    return True

print(my_function())

if my_function():
    print("YES!")
else:
    print("NO!")



# 6 Check if an object is an integer or not
x = 200
print(isinstance(x, int))