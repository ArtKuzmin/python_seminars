adress_book = dict()
counter = 1 # каунтер добавил, чтобы при добавлении новой записи после импорта из файла не было конфлита по id и перезаписи


def add_adress(adress):
    global counter
    global adress_book
    if counter < max(adress_book):
        counter = max(adress_book) + 1
    adress_book[counter] = (adress)
    print(adress_book)
    counter += 1


def delete_adress(id):
    global adress_book
    adress_book.pop(id)


def get_adress(id):
    global adress_book
    return adress_book.get(id)
