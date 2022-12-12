# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

#  Версия для двух человек

first_move = randint(1, 2)
print(f'{first_move} Player goes first!')
M = 28              # Параметры игры не стал во ввод запихивать
candies = 2021
player1_counter = 0  # Счетчик по условию не обязателен, но с ним нагляднее
player2_counter = 0
i = first_move

def que(i):
    global pl
    if i % 2 == 0:
        pl = 2
    else:
        pl = 1

def move(pl):    
    global candies
    global player1_counter
    global player2_counter

    while True:
        move = int(input(f"{pl} Player's move: "))
        if 0 < move < M + 1 and move <= candies:
            break
        else:
            print("Incorrect move, try again")
    if pl == 1:
        player1_counter += move
        print(f"{pl} Player have {player1_counter} candies")
    else:
        player2_counter += move
        print(f"{pl} Player have {player2_counter} candies")
    candies -= move
    print(f"{candies} candies left")

while candies > 0:
    que(i)
    move(pl)
    print("------")
    i += 1
print("1 Player wins! Congrats!" if i % 2 == 0 else "2 Player wins! Congrats!")


# Версия с ботом. Оптимальной стратегией является такая, что брать надо столько конфет, 
# чтобы потом оставалось кратное М+1 количество 

# first_move = randint(1, 2)

# print(f'{first_move} Player goes first!')
# M = 28
# candies = 2021
# player1_counter = 0
# player2_counter = 0
# i = first_move

# def que(i):
#     global pl
#     if i % 2 == 0:
#         pl = 2
#     else:
#         pl = 1

# def move(pl):
#     global candies
#     global player1_counter
#     global player2_counter
#     rand_move = 1

#     if pl == 1:
#         while True:
#             move = int(input(f"{pl} Player's move: "))
#             if 0 < move < M + 1 and move <= candies:
#                 break
#             else:
#                 print("Incorrect move, try again")
#         player1_counter += move
#         candies -= move
#         print(f"{pl} Player have {player1_counter} candies")
#         print(f"{candies} candies left")

#     else:
#         while (candies - rand_move) % (M + 1) != 0 and candies >= rand_move < M:
#             rand_move += 1       
#         print(f"{pl} Player took {rand_move} candies")
#         player2_counter += rand_move
#         candies -= rand_move
#         print(f"{pl} Player have {player2_counter} candies")
#         print(f"{candies} candies left")

# while candies > 0:
#     que(i)
#     move(pl)
#     print("------")
#     i += 1

# print("1 Player wins! Congrats!" if i % 2 == 0 else "2 Player wins! Congrats!")

# Версия, где два бота играю друг с другом (погонять тесты)

# first_move = randint(1, 2)

# print(f'{first_move} Player goes first!')
# candies = 2021
# player1_counter = 0
# player2_counter = 0
# i = first_move

# def que(i):
#     global pl
#     if i % 2 == 0:
#         pl = 2
#     else:
#         pl = 1

# def move(pl):
#     global candies
#     global player1_counter
#     global player2_counter
#     rand_move = 1 

#     while (candies - rand_move) % 29 != 0 and candies > rand_move < 28:
#             rand_move += 1
#     if pl == 1:
#             print(f"{pl} Player took {rand_move} candies")
#             player1_counter += rand_move
#             print(f"{pl} Player have {player1_counter} candies")
#     else:
#             print(f"{pl} Player took {rand_move} candies")
#             player2_counter += rand_move
#             print(f"{pl} Player have {player1_counter} candies")
#     candies -= rand_move        
#     print(f"{candies} candies left")

# while candies > 0:
#     que(i)
#     move(pl)
#     print("------")
#     i += 1
# print("1 Player wins! Congrats!" if i % 2 == 0 else "2 Player wins! Congrats!")
