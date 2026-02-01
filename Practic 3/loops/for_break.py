# for loop with break examples

#  1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

#  2
for i in range(10):
    if i == 4:
        break
    print(i)

#  3
for char in "python":
    if char == "h":
        break
    print(char)

#  4
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 3:
        break
    print(n)

#  5
for x in range(6):
    if x == 3:
        break
    print(x)
