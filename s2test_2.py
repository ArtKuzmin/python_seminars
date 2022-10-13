# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = (int(input("Input number: ")))
sum = 1
lst = []
for x in range(1, N+1):
    sum *= x  
    lst.append(sum)
print(lst)