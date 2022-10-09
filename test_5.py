#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from math import sqrt


x1, y1, x2, y2 = float(input("Input first X coordinate: ")), float(input("Input first Y coordinate: ")), float(input("Input second X coordinate: ")), float(input("Input second Y coordinate: "))
print(round(sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)) # почему при вводе первого тестого значения (3,6 и 2,1) округляется до одного знака? В остальных случаях 2 знака как и положено