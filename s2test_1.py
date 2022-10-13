# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
a = (input("Input number: "))
sum = 0
for i in a:
    if i == ".":
        continue
    sum += int(i)
print(sum)
