import backend
import json


def read_adress():
    with open("file.json", "r") as data:
        backend.adress_book = json.load(data)
    data.close


def write_adress():
    with open("file.json", "w") as data:
        json.dump(backend.adress_book, data)
    data.close
