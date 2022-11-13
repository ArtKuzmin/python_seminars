import backend


def read_adress():
    with open("file.txt", "r") as data:
        while True:
            line = data.readline()
            if not line:
                break
            t_line = line.strip().split(":")
            backend.adress_book[int(t_line[0])] = t_line[1]
    data.close


def write_adress():
    with open("file.txt", "a") as data:
        for key, value in backend.adress_book.items():
            data.write('%s:%s\n' % (key, value))
    data.close
