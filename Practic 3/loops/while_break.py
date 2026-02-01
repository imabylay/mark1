# while loop with break examples

# 1
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# 2
x = 0
while True:
    print(x)
    if x == 2:
        break
    x += 1

# 3
num = 1
while num <= 10:
    if num == 5:
        break
    print(num)
    num += 1

# 4
attempts = 0
while attempts < 5:
    print("Trying...")
    break

# 5
i = 0
while i < 10:
    if i == 7:
        break
    i += 1
    print(i)
