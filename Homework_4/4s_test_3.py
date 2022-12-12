# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
from random import randint

N = (int(input("Input number: ")))
lst = []
for i in range(0, N):
    lst.append(randint(0, N))
print(lst)

lst_unique = []
for i in range(0, len(lst)):
    t = True
    for j in range(0, len(lst)):
        if lst[i] == lst[j] and i != j:
            t = False
            break
    if t:
        lst_unique.append(lst[i])
print(lst_unique)
