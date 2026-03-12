import os

# 1. Создание вложенных каталогов
nested_dirs = "parent/child/grandchild"
os.makedirs(nested_dirs, exist_ok=True)
print(f"1. Созданы каталоги: {nested_dirs}")

# 2. Список файлов и папок в текущей директории
print("\n2. Содержимое текущей папки:")
items = os.listdir(".")
for item in items:
    print("   ", item)

# 3. Найти все файлы с расширением .txt в текущей папке
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
print("\n3. Все .txt файлы в текущей папке:")
for f in txt_files:
    print("   ", f)

# 4. Найти все файлы с расширением .py в папке file_handling (если она есть)
if os.path.exists("file_handling"):
    py_files = [f for f in os.listdir("file_handling") if f.endswith(".py")]
    print("\n4. .py файлы в папке file_handling:")
    for f in py_files:
        print("   ", f)
else:
    print("\n4. Папка file_handling не найдена.")