import os
import shutil

# Копирование и удаление файлов

source = "example.txt"  # файл, который создали в write_files.py
backup = "backup.txt"

# 1. Копирование файла
if os.path.exists(source):
    shutil.copy(source, backup)
    print(f"1. Файл {source} скопирован в {backup}")
else:
    print(f"1. Исходный файл {source} не найден, копирование не выполнено.")

# 2. Безопасное удаление (с проверкой существования)
file_to_delete = backup
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"2. Файл {file_to_delete} удалён.")
else:
    print(f"2. Файл {file_to_delete} не найден, удаление не требуется.")

# 3. Копирование целой папки (пример)
# Создадим временную папку и скопируем её
os.makedirs("temp_folder", exist_ok=True)
with open("temp_folder/test.txt", "w") as f:
    f.write("Тест")
shutil.copytree("temp_folder", "temp_folder_backup", dirs_exist_ok=True)
print("3. Папка temp_folder скопирована в temp_folder_backup")