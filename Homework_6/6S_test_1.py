#Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
#  Добавьте возможность использования скобок, меняющих приоритет операций. 

# print(eval((input("Input arithmetic expression: "))))

example = input("Input arithmetic expression: ")
result = 0
example_lst = []
digits = "1234567890"
operators = "+-/*"
number = ""
actions = 0

# Собираем строку в список по операторам и числам:
for i in example:
    if i in digits:
        number += i   
    if i in operators:
        example_lst.append(number)
        number = ""
        example_lst.append(i)   
        actions += 1
example_lst.append(number)

def pop_used_elements():
    example_lst.pop(i+1)
    example_lst.pop(i)
    example_lst[i-1] = result

while actions > 0:
    for i in range(len(example_lst)-1):
        result = 0
        if example_lst[i] == "*":
            result = float(example_lst[i-1]) * float(example_lst[i+1])
            pop_used_elements()
            break
    for i in range(len(example_lst)-1):
        result = 0
        if example_lst[i] == "/":
            result = float(example_lst[i-1]) / float(example_lst[i+1])
            pop_used_elements()
            break
    for i in range(len(example_lst)-1):
        result = 0
        if example_lst[i] == "+":
            result = float(example_lst[i-1]) + float(example_lst[i+1])
            pop_used_elements()
            break
        elif example_lst[i] == "-":
            result = float(example_lst[i-1]) - float(example_lst[i+1])
            pop_used_elements()
            break
    actions -= 1

print(example, " = ", round(result, 2))

