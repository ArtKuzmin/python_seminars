# Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x, y = int(input("Input non-zero X coordinate: ")), int(input("Input non-zero Y coordinate: "))
if x == 0 or y == 0:
    print("One or both coordinates are 0. Input again")
elif x > 0 and y > 0:
    print("1 quarter")
elif x < 0 and y > 0:
    print("2 quarter")
elif x < 0 and y < 0:
    print("3 quarter")
else:
    print("4 quarter")
