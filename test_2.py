# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#from operator import truediv


x, y, z = (input("Input X - 1 for true or 0 for false: ")), (input("Input Y - 1 for true or 0 for false: ")), (input("Input Z - 1 for true or 0 for false: "))
if x == "1":
    x = True
else:
    x = False
if y == "1":
    y = True
else:
    y = False
if z == "1":
    z = True
else:
    z = False
print(not (x or y or z))
print(not x and not y and not z)
