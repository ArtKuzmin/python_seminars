#  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = (int(input("Input number: ")))
lst = []
i = 2
while N > 1:
    if N % i == 0:
        lst.append(i)
        N /= i
    else:
        i += 1
print(lst)
