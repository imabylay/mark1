# Запись и добавление в файлы

filename = "example.txt"

# 1. Запись в файл (режим 'w') – перезаписывает файл
print("1. Записываем данные в файл (режим 'w'):")
with open(filename, "w", encoding="utf-8") as f:
    f.write("Строка, записанная первой.\n")
    f.write("Вторая строка.\n")
print("Файл записан. Содержимое:")
with open(filename, "r") as f:
    print(f.read())

# 2. Добавление в конец файла (режим 'a')
print("\n2. Добавляем новые строки (режим 'a'):")
with open(filename, "a", encoding="utf-8") as f:
    f.write("Это добавленная строка.\n")
    f.write("И ещё одна.\n")
print("Теперь файл содержит:")
with open(filename, "r") as f:
    print(f.read())

# 3. Создание нового файла (режим 'x') – если файл уже существует, будет ошибка
try:
    with open("new_file.txt", "x", encoding="utf-8") as f:
        f.write("Совершенно новый файл.\n")
    print("\n3. Файл new_file.txt успешно создан.")
except FileExistsError:
    print("\n3. Файл new_file.txt уже существует, не стали перезаписывать.")