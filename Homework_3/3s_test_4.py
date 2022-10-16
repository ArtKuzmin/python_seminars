# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

N = (int(input("Input number: ")))
# Ниже закомментирован простой способ через встроенную библиотеку:
# print(bin(N).replace("0b", ""))
bin_num = ""
if (N != 0):
    while (N > 0):
        if (N % 2 == 0):
            bin_num = "0" + bin_num
            N = N/2
        else:
            bin_num = "1" + bin_num
            N = int(N/2)
else:
    bin_num = "0"
print(bin_num)