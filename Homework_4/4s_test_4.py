# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0
from random import randint
k = (int(input("Input coefficient: ")))
lst = []
polynom = ""
for i in range(k, -1, -1):
    r = randint(0, 100)
    if r == 1:
        lst.append("x^%d " % (k))
    elif r == 0:
        continue
    elif k == 0:
        lst.append("%d" % (r))
    elif k == 1:
        lst.append("%d*x " % (r))
    else:
        lst.append("%d*x^%d " % (r,  k))
    k -= 1
polynom = "+ ".join(lst)
polynom += " = 0"
print(polynom)
with open("polynom.txt", "a") as data:
    data.write(polynom + "\n")
    data.close
