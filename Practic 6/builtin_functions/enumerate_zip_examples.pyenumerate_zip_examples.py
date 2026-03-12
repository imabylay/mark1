# enumerate и zip

# 1. enumerate – получить индекс при итерации
fruits = ["яблоко", "банан", "апельсин"]
print("1. Перечисление фруктов с индексами:")
for idx, fruit in enumerate(fruits):
    print(f"   {idx}: {fruit}")

# Можно начать с другого числа
print("\n   С нумерацией с 1:")
for idx, fruit in enumerate(fruits, start=1):
    print(f"   {idx}: {fruit}")

# 2. zip – объединить два списка в пары
names = ["Анна", "Борис", "Виктор"]
scores = [85, 92, 78]

print("\n2. Пары имя-балл через zip:")
for name, score in zip(names, scores):
    print(f"   {name}: {score}")

# 3. zip с тремя списками
years = [2021, 2022, 2023]
print("\n3. Тройки имя-балл-год:")
for name, score, year in zip(names, scores, years):
    print(f"   {name}: {score} ({year})")

# 4. Создание словаря из двух списков
dict_from_zip = dict(zip(names, scores))
print("\n4. Словарь из zip:")
print("   ", dict_from_zip)