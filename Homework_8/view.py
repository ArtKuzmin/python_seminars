import sqlite3
import pandas as pd

def menu():    
        print("""Что вы хотите сделать?\n
        1. Создать дефолтную таблицу
        2. Добавить сотрудника
        3. Удалить запись о сотрудникк по известному id
        4. Изменить данные о сотруднике по известному id        
        5. Вывести все записи (Осторожно, может быть много записей!)
        0. Завершить программу""")

def edit_menu():
    print('''Что вы хотите изменить?\n
      1. Имя
      2. Фамилию
      3. Возраст
      4. Отдел
      5 Телефон''')

def print_db():
    conn = sqlite3.connect('personal.db')
    print(pd.read_sql_query("SELECT * FROM employees", conn))
    conn.close()