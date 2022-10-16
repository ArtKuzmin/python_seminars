# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def n_fib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return (-1)**(n+1) * fib(n)


k = (int(input("Input number: ")))
lst_fib = []
for i in range(k, 0, -1):
    lst_fib.append(n_fib(i))
for i in range(0, k+1):
    lst_fib.append(fib(i))
print(lst_fib)