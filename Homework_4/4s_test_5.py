#  Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

lst = []
with open("polynom.txt", "r") as data:
    lst = data.readlines()
    lst = [line.rstrip() for line in lst]
    data.close

lst_1 = lst[0].split(" + ")
lst_2 = lst[1].split(" + ")
lst_1[len(lst_1) - 1] = lst_1[len(lst_1) - 1][:-4]
lst_2[len(lst_2) - 1] = lst_2[len(lst_2) - 1][:-4]
print(lst_1)
print(lst_2)
for i in range(0, len(lst_2)):
    s = 0
    t1 = lst_2[i][lst_2[i].find(start := "")+len(start):lst_2[i].find('*')]
    for j in range(0, len(lst_1)):
        t2 = lst_1[j][lst_1[j].find(start := "")+len(start):lst_1[j].find('*')]
        if (lst_2[i][-1]) == "x" and (lst_1[j][-1]) == "x":
            s = (int(t2) + int(t1))
            lst_2[i] = str(s) + lst_2[i][2:]
        elif lst_2[i].isdigit() and lst_1[j].isdigit():
            t = int(lst_2[5]) + int(lst_1[3])
            lst_2[i] = str(t)
        elif (lst_2[i][-1]) == (lst_1[j][-1]) and lst_1[j].isdigit() == False:
            s = int(t2) + int(t1)
            lst_2[i] = str(s) + lst_2[i][2:]
print("-----------")
final_lst = " + ".join(lst_2)
final_lst += " = 0"
print(final_lst)
with open("polynom_sum.txt", "w") as data:
    data.write(final_lst + "\n")
    data.close
