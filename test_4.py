#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
a = int(input("Input quarter number: "))
if a != 1 and a != 2 and a != 3 and a != 4:
    print("Incorrect quarter number. Input again")
elif a == 1:
    print("X > 0; Y > 0")
elif a == 2:
    print("X < 0; Y > 0")
elif a == 3:
    print("X < 0; Y < 0")
else:
    print("X > 0; Y < 0")