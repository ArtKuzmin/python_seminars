import IO
import backend


def add_adress():
    backend.add_adress(input(
        "Введите Имя, фамилию, дату рождения, место работы и телефоны через пробел: "))


def delete_adress():
    id = input("Введите Введите id, который вы хотите удалить: ")
    backend.delete_adress(id)
    return f"Запись с id {id} удалена"


def get_adress():
    id = input("Введите Введите id, который вы хотите получить: ")
    data = backend.get_adress(id)
    if data == None:
        return f"Нет записи с таким id {id}"
    else:
        return data


def read_adress():
    IO.read_adress()


def write_adress():
    IO.write_adress()
