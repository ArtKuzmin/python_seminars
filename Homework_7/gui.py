import UI
import backend
import pprint


def gui():
    while True:
        print("""Что вы хотите сделать?\n 1. Добавить адрес\n 2. Удалить адрес по известному id 
 3. Получить информацию по известному id\n 4. Считать данные из файла\n 5. Записать данные в файл
 6. Вывести все записи (Осторожно, может быть много записей!)\n 7. Завершить программу""")

        match input():
            case "1":
                UI.add_adress()
                print("Запись добавлена в телефонный справочник")
            case "2":
                print(UI.delete_adress())
            case "3":
                print(UI.get_adress())
            case "4":
                UI.read_adress()
                print("Данные с файла считаны")
            case "5":
                UI.write_adress()
                print("Данные записаны в файл")
            case "6":
                pprint.pprint(sorted(backend.adress_book.items()))
            case "7":
                print("Программа завершена")
                exit()
