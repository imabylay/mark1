import psycopg2
import csv
import os
from config import load_config

class PhoneBook:
    def __init__(self):
        """Инициализация подключения к БД"""
        self.conn = None
        self.connect()
        self.create_table()
    
    def connect(self):
        """Подключение к PostgreSQL"""
        try:
            params = load_config()
            self.conn = psycopg2.connect(**params)
            print("✅ Подключено к базе данных")
        except Exception as e:
            print(f"❌ Ошибка подключения: {e}")
            raise
    
    def create_table(self):
        """Создание таблицы для телефонной книги"""
        sql = """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                self.conn.commit()
                print("✅ Таблица phonebook готова")
        except Exception as e:
            print(f"❌ Ошибка создания таблицы: {e}")
    
    def insert_from_csv(self, filename):
        """Вставка данных из CSV файла"""
        if not os.path.exists(filename):
            print(f"❌ Файл {filename} не найден")
            return
        
        sql = "INSERT INTO phonebook (name, phone) VALUES (%s, %s)"
        try:
            with self.conn.cursor() as cur:
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader)  # пропускаем заголовок если есть
                    count = 0
                    for row in reader:
                        if len(row) >= 2:
                            try:
                                cur.execute(sql, (row[0].strip(), row[1].strip()))
                                count += 1
                            except psycopg2.IntegrityError:
                                print(f"⚠️ Телефон {row[1]} уже существует, пропущен")
                                self.conn.rollback()
                            except Exception as e:
                                print(f"⚠️ Ошибка при вставке {row}: {e}")
                                self.conn.rollback()
                self.conn.commit()
                print(f"✅ Добавлено {count} контактов из CSV")
        except Exception as e:
            print(f"❌ Ошибка чтения CSV: {e}")
    
    def insert_from_console(self):
        """Вставка данных, введенных с консоли"""
        print("\n--- Добавление нового контакта ---")
        name = input("Введите имя: ").strip()
        phone = input("Введите номер телефона: ").strip()
        
        if not name or not phone:
            print("❌ Имя и телефон не могут быть пустыми")
            return
        
        sql = "INSERT INTO phonebook (name, phone) VALUES (%s, %s)"
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql, (name, phone))
                self.conn.commit()
                print(f"✅ Контакт '{name}' добавлен")
        except psycopg2.IntegrityError:
            print(f"❌ Ошибка: Телефон {phone} уже существует в базе")
            self.conn.rollback()
        except Exception as e:
            print(f"❌ Ошибка: {e}")
    
    def update_contact(self):
        """Обновление имени или телефона контакта"""
        print("\n--- Обновление контакта ---")
        search = input("Введите имя или телефон для поиска: ").strip()
        
        # Сначала найдем контакт
        sql_find = "SELECT id, name, phone FROM phonebook WHERE name = %s OR phone = %s"
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql_find, (search, search))
                contact = cur.fetchone()
                
                if not contact:
                    print(f"❌ Контакт '{search}' не найден")
                    return
                
                print(f"\nНайден контакт: ID={contact[0]}, Имя={contact[1]}, Телефон={contact[2]}")
                print("Что обновить?")
                print("1. Имя")
                print("2. Телефон")
                print("3. Имя и телефон")
                
                choice = input("Выберите (1/2/3): ").strip()
                
                if choice == '1':
                    new_name = input("Введите новое имя: ").strip()
                    if new_name:
                        sql_update = "UPDATE phonebook SET name = %s WHERE id = %s"
                        cur.execute(sql_update, (new_name, contact[0]))
                        self.conn.commit()
                        print(f"✅ Имя обновлено на '{new_name}'")
                elif choice == '2':
                    new_phone = input("Введите новый телефон: ").strip()
                    if new_phone:
                        sql_update = "UPDATE phonebook SET phone = %s WHERE id = %s"
                        cur.execute(sql_update, (new_phone, contact[0]))
                        self.conn.commit()
                        print(f"✅ Телефон обновлен на '{new_phone}'")
                elif choice == '3':
                    new_name = input("Введите новое имя: ").strip()
                    new_phone = input("Введите новый телефон: ").strip()
                    if new_name and new_phone:
                        sql_update = "UPDATE phonebook SET name = %s, phone = %s WHERE id = %s"
                        cur.execute(sql_update, (new_name, new_phone, contact[0]))
                        self.conn.commit()
                        print(f"✅ Контакт обновлен: {new_name} - {new_phone}")
                else:
                    print("❌ Неверный выбор")
                    
        except Exception as e:
            print(f"❌ Ошибка: {e}")
    
    def search_contacts(self):
        """Поиск контактов с фильтрами"""
        print("\n--- Поиск контактов ---")
        print("1. По имени (точное совпадение)")
        print("2. По имени (частичное совпадение)")
        print("3. По телефону")
        print("4. По префиксу телефона")
        print("5. Показать все контакты")
        
        choice = input("Выберите (1/2/3/4/5): ").strip()
        
        try:
            with self.conn.cursor() as cur:
                if choice == '1':
                    name = input("Введите имя: ").strip()
                    cur.execute("SELECT * FROM phonebook WHERE name = %s ORDER BY name", (name,))
                elif choice == '2':
                    name = input("Введите часть имени: ").strip()
                    cur.execute("SELECT * FROM phonebook WHERE name LIKE %s ORDER BY name", (f"%{name}%",))
                elif choice == '3':
                    phone = input("Введите телефон: ").strip()
                    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
                elif choice == '4':
                    prefix = input("Введите префикс (например +7, 8): ").strip()
                    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s ORDER BY name", (f"{prefix}%",))
                elif choice == '5':
                    cur.execute("SELECT * FROM phonebook ORDER BY name")
                else:
                    print("❌ Неверный выбор")
                    return
                
                results = cur.fetchall()
                if results:
                    print(f"\n📞 Найдено {len(results)} контактов:")
                    print("-" * 50)
                    for row in results:
                        print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]} | Создан: {row[3]}")
                    print("-" * 50)
                else:
                    print("❌ Контакты не найдены")
                    
        except Exception as e:
            print(f"❌ Ошибка: {e}")
    
    def delete_contact(self):
        """Удаление контакта по имени или телефону"""
        print("\n--- Удаление контакта ---")
        search = input("Введите имя или телефон для удаления: ").strip()
        
        sql = "DELETE FROM phonebook WHERE name = %s OR phone = %s RETURNING id, name, phone"
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql, (search, search))
                deleted = cur.fetchone()
                self.conn.commit()
                
                if deleted:
                    print(f"✅ Удален контакт: ID={deleted[0]}, Имя={deleted[1]}, Телефон={deleted[2]}")
                else:
                    print(f"❌ Контакт '{search}' не найден")
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            self.conn.rollback()
    
    def show_menu(self):
        """Показать главное меню"""
        print("\n" + "=" * 50)
        print("📞 ТЕЛЕФОННАЯ КНИГА 📞")
        print("=" * 50)
        print("1. Добавить контакт (с консоли)")
        print("2. Импорт из CSV файла")
        print("3. Обновить контакт")
        print("4. Поиск контактов")
        print("5. Удалить контакт")
        print("6. Показать все контакты")
        print("0. Выход")
        print("=" * 50)
    
    def run(self):
        """Запуск приложения"""
        while True:
            self.show_menu()
            choice = input("Выберите действие: ").strip()
            
            if choice == '1':
                self.insert_from_console()
            elif choice == '2':
                filename = input("Введите имя CSV файла (например contacts.csv): ").strip()
                self.insert_from_csv(filename)
            elif choice == '3':
                self.update_contact()
            elif choice == '4':
                self.search_contacts()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                # Быстрый показ всех контактов
                try:
                    with self.conn.cursor() as cur:
                        cur.execute("SELECT * FROM phonebook ORDER BY name")
                        results = cur.fetchall()
                        if results:
                            print(f"\n📞 Всего контактов: {len(results)}")
                            print("-" * 50)
                            for row in results:
                                print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
                            print("-" * 50)
                        else:
                            print("📭 Телефонная книга пуста")
                except Exception as e:
                    print(f"❌ Ошибка: {e}")
            elif choice == '0':
                print("👋 До свидания!")
                if self.conn:
                    self.conn.close()
                break
            else:
                print("❌ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    pb = PhoneBook()
    pb.run()