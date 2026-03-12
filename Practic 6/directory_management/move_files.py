import os
import shutil

# Перемещение и копирование файлов между каталогами

# Создадим тестовые папки и файл
os.makedirs("source_folder", exist_ok=True)
os.makedirs("dest_folder", exist_ok=True)

test_file = "source_folder/move_me.txt"
with open(test_file, "w") as f:
    f.write("Этот файл будет перемещён.")

# 1. Перемещение файла
shutil.move(test_file, "dest_folder/move_me.txt")
print("1. Файл перемещён из source_folder в dest_folder")

# 2. Копирование файла с новым именем
shutil.copy("dest_folder/move_me.txt", "dest_folder/copy_of_moved.txt")
print("2. Создана копия файла внутри dest_folder")

# 3. Перемещение целой папки (если нужно)
shutil.move("source_folder", "dest_folder/source_folder")
print("3. Папка source_folder перемещена внутрь dest_folder")