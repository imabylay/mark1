# 1
x = 10
y = 3.14
z = 2j

print(type(x))  # int
print(type(y))  # float
print(type(z))  # complex



# 2
a = 999999999999999999999
b = -42

print(a)
print(b)
print(type(a))



# 3
x = 5.5
y = 2e3      # 2000.0
z = -1.2E2   # -120.0

print(x, y, z)
print(type(y))



# 4
x = 7
y = 4.9

a = float(x)
b = int(y)
c = complex(x)

print(a)       # 7.0
print(b)       # 4
print(c)       # (7+0j)



# 5
import random

number = random.randrange(1, 10)
print(number)
