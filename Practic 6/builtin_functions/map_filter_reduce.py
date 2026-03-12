from functools import reduce

# Примеры map, filter, reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. map – применить функцию ко всем элементам
squared = list(map(lambda x: x**2, numbers))
print("1. Квадраты чисел через map:")
print("   ", squared)

# 2. filter – оставить только чётные
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("\n2. Чётные числа через filter:")
print("   ", evens)

# 3. reduce – свернуть список (например, сумма)
sum_all = reduce(lambda a, b: a + b, numbers)
print("\n3. Сумма всех чисел через reduce:")
print("   ", sum_all)

# 4. reduce – произведение
product = reduce(lambda a, b: a * b, numbers[:5])  # только первые 5 чтобы не было огромно
print("\n4. Произведение первых 5 чисел через reduce:")
print("   ", product)