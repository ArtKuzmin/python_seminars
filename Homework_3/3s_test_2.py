# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint
# Возьмем код из прошлого дз для создания рандомного списка с длиной, запрашиваемой у пользователя, и выведем его
N = (int(input("Input number: ")))
lst = []
for i in range(0, N):
    lst.append(randint(-N, N))
print(lst)
# ----
lst_pair_sum = []
for j in range(0, int(len(lst)/2)):
    lst_pair_sum.append(lst[j] * lst[len(lst)-1 - j])
if len(lst) % 2 != 0:
    lst_pair_sum.append((lst[int((len(lst)/2))]**2))
print(lst_pair_sum)