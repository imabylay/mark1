# Shorthand if statements and ternary operators

# 1
a = 5
b = 2
if a > b: print("a is greater than b")

# 2
a = 2
b = 330
print("A") if a > b else print("B")

# 3
x = 10
y = 20
bigger = x if x > y else y
print("Bigger is", bigger)

# 4
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

# 5
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
