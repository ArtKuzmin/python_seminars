# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint
# Возьмем код из прошлого дз для создания рандомного списка с длиной, запрашиваемой у пользователя, и выведем его
N = (int(input("Input number: ")))
lst = []
for i in range(0, N):
    lst.append(randint(-N, N))
print(lst)
# ----
sum = 0
for j in range(1, len(lst), 2):
    sum += lst[j]
print(sum)