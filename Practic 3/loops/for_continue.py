# for loop with continue examples

#  1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

#  2
for i in range(6):
    if i == 2:
        continue
    print(i)

#  3
for char in "python":
    if char == "o":
        continue
    print(char)

#  4
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        continue
    print("Odd:", n)

#  5
for x in range(5):
    if x == 4:
        continue
    print(x)
