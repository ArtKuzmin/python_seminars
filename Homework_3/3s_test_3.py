# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import random

# Возьмем код из прошлого дз для создания рандомного списка с длиной, запрашиваемой у пользователя, и выведем его
N = (int(input("Input number: ")))
lst = []
for i in range(0, N):
    lst.append(round((random() * N), 3))
print(lst)
# ---

for j in range(len(lst)):    
    lst[j] = round((lst[j] - int(lst[j])),3) # округления использовал дважды, т.к. без него в этой строке оказывается гораздо 
print(max(lst) - min(lst))                      #больше знаков после запято (из-за апроксимации как я полагаю)
# закомментил более длинное решение 
# lst_min = lst[i]
# lst_max = lst[i]
# for i in range(len(lst)):    
#     # if lst_min > lst[i]:
#     #     lst_min = lst[i] 
#     # if lst_max < lst[i]:
#     #     lst_max = lst[i] 
# print(lst_min - lst_max)