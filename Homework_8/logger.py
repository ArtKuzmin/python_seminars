from datetime import datetime as dt
from time import time
import backend

def adding_entry_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; Запись добавлена: {}\n'.format(time, data))
    file.close()

def deletion_logger(data):
    
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; Удалена запись с id: {}\n'.format(time, data))
    file.close()

def editing_entry_logger(data):
   
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; Запись изменена (столбец, значение, id);{}\n'
                    .format(time, data))
    file.close()