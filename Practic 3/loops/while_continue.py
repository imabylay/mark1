# while loop with continue examples

#  1
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#  2
x = 0
while x < 5:
    x += 1
    if x % 2 == 0:
        continue
    print("Odd:", x)

#  3
num = 0
while num < 10:
    num += 1
    if num > 7:
        continue
    print(num)

#  4
i = 0
while i < 4:
    i += 1
    if i == 2:
        continue
    print("Value:", i)

#  5
count = 0
while count < 5:
    count += 1
    if count == 4:
        continue
    print(count)
