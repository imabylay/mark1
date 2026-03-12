# Чтение файлов разными способами

# Создаём тестовый файл, если его нет
import os

filename = "sample.txt"
if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Первая строка\n Вторая строка\n Третья строка")

# 1. Чтение всего файла целиком
print("1. Чтение всего файла:")
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 2. Чтение построчно в цикле
print("\n2. Чтение построчно:")
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")  # end="" чтобы не было лишних пустых строк

# 3. Чтение всех строк в список
print("\n3. Чтение в список строк:")
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

# 4. Чтение одной строки (первой)
print("\n4. Чтение одной строки (первой):")
with open(filename, "r", encoding="utf-8") as f:
    first_line = f.readline()
    print(first_line, end="")