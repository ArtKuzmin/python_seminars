# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
import os.path

def code_to_rle(string_to_arch):
    arch_string = ""
    i = 0
    while (i < len(string_to_arch)):
        counter = 1
        ch = string_to_arch[i]
        j = i
        while (j < len(string_to_arch)-1):
            if (string_to_arch[j] == string_to_arch[j + 1]):
                counter = counter + 1
                j += 1
            else:
                break
        arch_string += str(counter) + "*" + ch + "|"
        i = j + 1
    return arch_string

def decode_rle(coded_string):
    coded_list = []
    coded_list_temp = coded_string.split("|")
    for i in range(len(coded_list_temp)-1):
        coded_list.append(tuple(coded_list_temp[i].split("*")))
    for i in coded_list:
        print(int(i[0]) * i[1], end="")
    print()

string_to_arch = "AAAAAAAAAAAAAAAAAAAAAAAaaaaaaa11111111111ssssddddddssss"
coded_string = code_to_rle(string_to_arch)
print(string_to_arch)
print(coded_string)
decode_rle(coded_string)

# with open("file.txt", "w") as data:  # разница в размере между исходной и сжатой строкой 55 - 26 = 29 байт
#     data.write(str(coded_string))
#     data.close
# print(os.path.getsize("file.txt"))
