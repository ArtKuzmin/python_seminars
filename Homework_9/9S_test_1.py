#Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

from tkinter import *
from random import *

pl = randint(1, 2)
print(f'{pl} Player goes first!')
global i
i = pl
root = Tk()
root.title('Крестики - нолики')
game_run = True


def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True


def que(i):
    global pl
    if i % 2 == 0:
        pl = 2
    else:
        pl = 1


def click(row, col):
    global i
    que(i)
    if game_run and field[row][col]['text'] == ' ':
        if pl == 1:
            i += 1
            field[row][col]['text'] = 'X'
            check_win('X')
        if pl == 2:
            field[row][col]['text'] = 'O'
            i += 1
            check_win('O')


def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)


def check_line(a1, a2, a3, smb):
    global game_run
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        game_run = False


field = []
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()
