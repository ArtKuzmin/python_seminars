# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
N = (int(input("Input number: ")))
sum = 0
for x in range(1, N+1):
    sum += (1 + 1/x)**x     
print(sum)