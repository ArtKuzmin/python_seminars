import sqlite3
import UI
import logger

conn = sqlite3.connect('personal.db')
c = conn.cursor()
def create_db():
   global conn 
   conn = sqlite3.connect('personal.db')
   global c 
   c = conn.cursor()
   c.execute("""CREATE TABLE IF NOT EXISTS employees(
      employee_id INT PRIMARY KEY,
      Имя TEXT,
      Фамилия TEXT,
      Возраст INT,
      Отдел TEXT,
      Телефон INT);
      """)
   c.executemany('INSERT or IGNORE into employees VALUES (?, ?, ?, ?, ?, ?)',
      [(1, 'Артем', 'Иванов', 34, 'Backend', 9132316750),
      (2, 'Иван', 'Сидоров', 23, 'Frontend', 9124333655),
      (3, 'Сергей', 'Кузнецов', 22, 'Support', 9113453633),
      (4, 'Андрей', 'Медведев', 18, 'Frontend', 9624567333),
      (5, 'Алексей', 'Смирнов', 54, 'Backend', 9234566543)])
   conn.commit()

def insert_entry():
   entry = UI.add_employee() 
   c.execute("INSERT or IGNORE into employees VALUES (?, ?, ?, ?, ?, ?);", entry)
   conn.commit()
   print("Запись успешно добавлена")
   logger.adding_entry_logger(entry)
    
def delete_employee():
    id = UI.delete_employee()  
    c.execute("DELETE from employees where employee_id = ?", (id,))
    conn.commit()
    print("Запись успешно удалена")
    logger.deletion_logger(id)
 
def edit_employee():
   edited_values = UI.edit_employee()                  
   c.execute(f"Update employees set {edited_values[0]} = ? where employee_id = ?", (edited_values[1], edited_values[2]))
   conn.commit()
   print("Запись успешно изменена")
   logger.editing_entry_logger(edited_values)
   


















# # adress_book = dict()
# # counter = 1  # каунтер добавил, чтобы при добавлении новой записи после импорта из файла не было конфлита по id и перезаписи


# # def add_adress(adress):
# #     global counter
# #     global adress_book
# #     if not adress_book:
# #         counter = 1
# #     else:
# #         counter = int(max(adress_book)) + 1
# #     adress_book[str(counter)] = [adress.split(" ")]
# #     counter += 1


# # def delete_adress(id):
# #     global adress_book
# #     adress_book.pop(id)


# # def get_adress(id):
# #     global adress_book
# #     return adress_book.get(id)

