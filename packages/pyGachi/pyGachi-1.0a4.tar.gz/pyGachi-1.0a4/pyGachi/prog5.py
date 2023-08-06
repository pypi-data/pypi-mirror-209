import sqlite3

# Создание базы данных и таблицы для студентов
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 full_name TEXT,
                 address TEXT,
                 phone TEXT)''')
conn.commit()

# Функция для ввода информации о студентах
def input_student_data():
    full_name = input("Введите ФИО студента: ")
    address = input("Введите адрес студента: ")
    phone = input("Введите телефон студента: ")

    # Вставка данных в таблицу
    cursor.execute("INSERT INTO students (full_name, address, phone) VALUES (?, ?, ?)",
                   (full_name, address, phone))
    conn.commit()
    print("Данные студента успешно добавлены в базу данных.")

# Функция для вывода содержимого базы данных
def print_database_content():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) > 0:
        print("Содержимое базы данных:")
        for row in rows:
            print("ID:", row[0])
            print("ФИО:", row[1])
            print("Адрес:", row[2])
            print("Телефон:", row[3])
            print("------------------")
    else:
        print("База данных пуста.")

# Использование функций для ввода данных и вывода содержимого базы данных
while True:
    print('Выберите действие:')
    print('1: Добавить нового студента')
    print('2: Вывести всех студентов')
    print('3: Завершить работу')
    inp = int(input())
    if inp != 1 and inp != 2 and inp != 3:
        print('Введено неверное действие')
    if inp == 1:
        input_student_data()
    if inp == 2:
        print_database_content()
    if inp == 3:
        conn.close()
        break
