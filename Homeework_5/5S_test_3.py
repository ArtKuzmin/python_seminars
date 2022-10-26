# Создайте программу для игры в ""Крестики-нолики"".
from random import randint

first_move = randint(1, 2)
print(f'{first_move} Player goes first!')
i = first_move
matrix = [["-" for x in range(3)] for y in range(3)]
t = False

def que(i):
    global pl
    if i % 2 == 0:
        pl = 2
    else:
        pl = 1

def move(pl):
    move_x = 0
    move_y = 0
    while True:
        move_x,  move_y = int(input(f"Input X coordinate of your move: ")), int(
            input(f"Input Y coordinate of your move: "))
        if 0 <= move_x and move_y < 3 and (matrix[move_x][move_y]) == "-":
            break
        else:
            print("Incorrect move, try again")
    if pl == 1:
        matrix[move_x][move_y] = "O"
    else:
        matrix[move_x][move_y] = "X"

def line_ch(matrix):
    global t
    if (matrix[0][0] == matrix[0][1] and matrix[0][0] != "-") and (matrix[0][1] == matrix[0][2] and matrix[0][1] != "-"):
        t = True
    elif (matrix[1][0] == matrix[1][1] and matrix[1][0] != "-") and (matrix[1][1] == matrix[1][2] and matrix[1][1] != "-"):
        t = True
    elif (matrix[2][0] == matrix[2][1] and matrix[0][2] != "-") and (matrix[2][1] == matrix[2][2] and matrix[1][2] != "-"):
        t = True
    else:
        t = False

def row_ch(matrix):
    global t
    if (matrix[0][0] == matrix[0+1][0] and matrix[0][0] != "-") and (matrix[1][0] == matrix[1+1][0] and matrix[0][1] != "-"):
        t = True
    elif (matrix[0][1] == matrix[0+1][1] and matrix[1][0] != "-") and (matrix[1][1] == matrix[1+1][1] and matrix[1][1] != "-"):
        t = True
    elif (matrix[0][2] == matrix[0+1][2] and matrix[0][2] != "-") and (matrix[1][2] == matrix[1+1][2] and matrix[1][2] != "-"):
        t = True
    else:
        t = False

def diag_ch(matrix):
    global t
    if (matrix[0][0] == matrix[1][1] and matrix[0][0] != "-") and (matrix[1][1] == matrix[2][2] and matrix[1][1] != "-"):
        t = True

def rev_diag_ch(matrix):
    global t
    if (matrix[2][0] == matrix[1][1] and matrix[0][0] != "-") and (matrix[1][1] == matrix[0][2] and matrix[1][1] != "-"):
        t = True

def is_win(matrix):
    global t
    line_ch(matrix)
    if t:
        return
    row_ch(matrix)
    if t:
        return
    diag_ch(matrix)
    if t:
        return
    rev_diag_ch(matrix)
    if t:
        return

while True:
    que(i)
    move(pl)
    for s in matrix:
        print(*s)
    is_win(matrix)
    if t:
        print("1 Player wins! Congrats!" if i %
              2 != 0 else "2 Player wins! Congrats!")
        break
    i += 1

# Изначально хотел реализовать способ ниже, но так и не вышло заставить код работать. 
# Диагональные проверки и со строками вроде как работали (хоть и там иногда вылезали неверные выводы), 
# но вот со столбцами я долго промучился, но так и не добился результата. 
# В таком случае бы проверки работали для поля любого размера, а сам код был бы компактнее. 

# def line_ch(matrix):
#     global t
#     for r in range(m):
#         t = True
#         for c in range(m-1):
#             if matrix[r][c] != matrix[r][c+1] and matrix[r][c] != "-":
#                 t = False
#                 break

# def row_ch(matrix):
#     global t
#     for r in range(m):
#         t = True
#         for c in range(m-1):
#             if matrix[c][r] != matrix[c+1][r] and matrix[r][c] != "-":
#                 t = False
#                 break

# def diag_ch(matrix):
#     global t
#     for r in range(m-1):
#         t = True
#         if matrix[r][r] != matrix[r+1][r+1] and matrix[r][r] != "-":
#             t = False
#             break

# def rev_diag_ch(matrix):
#     global t
#     for r in range(m-1):
#         t = True
#         for c in range(m-1):
#             if matrix[r][n - c] != matrix[r+1][n - c - 1] and matrix[r][c] != "-":
#                 t = False
#                 break

# def is_win(matrix):
#     global t    
#     line_ch(matrix)
#     if t:        
#         return
#     row_ch(matrix)
#     if t:        
#         return            
#     diag_ch(matrix)
#     if t:        
#         return
#     rev_diag_ch(matrix)
#     if t:          
#         return