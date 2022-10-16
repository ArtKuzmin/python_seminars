# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

N = (int(input("Input number: ")))
res = 1
lst = []
for i in range(0, N):
    lst.append(randint(-N, N))
#print(lst) добавлял вывод списка, чтобы можно было проверить правильность результата
indesies = open("file.txt").read().split()
indesies = [int(i) for i in indesies] #вроде пишут, что самый простой и распространенный способ приведения строкового списка к целочисленному, но мне сначала думалось, что это можно делать при обращении итератора к элементу списка:/
for j in indesies:
    if j < N:
        res *= lst[j]
    else:
        continue
print(res)