# Basic while loop examples

# 1: print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# 2: countdown
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1

# 3: loop with condition
x = 0
while x < 10:
    print("x is", x)
    x += 2

# 4: user-like simulation
attempts = 0
while attempts < 3:
    print("Attempt", attempts + 1)
    attempts += 1

# 5: while with else
n = 1
while n < 4:
    print(n)
    n += 1
else:
    print("Loop finished")
