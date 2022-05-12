import re
import random


def field_for_game():
    print("Игровое поле:\r")
    field = [['f', '1', '2', '3'], ['1', '-', '-', '-'], ['2', '-', '-', '-'], ['3', '-', '-', '-']]
    for row in field:
        for x in row:
            print("{:4s}".format(x), end="")
        print()
    return field


def ask_figure():
    symbol = ""
    flag_figure = False
    while not flag_figure:
        print("Каким символом желаете ходить? X или O\r")
        symbol = input()
        if symbol.upper() == "X" or symbol.upper() == "O":
            flag_figure = True
    return symbol


def ask_game_move():
    position = ""
    flag_cord = False
    while not flag_cord:
        print("Ходите (Введите координату через пробел):\r")
        position = input()
        if not re.match('^[1-3] [1-3]$', position):
            print("Паттерн строки не совпадает. Введите координаты через пробел. Они не должны выходить за границы "
                  "игрового поля:\r")
        else:
            flag_cord = True
    return position


def who_first():
    if random.randint(0, 1) == 0:
        print("Игрок 1 - ходит первым\r")
        return 0
    else:
        print("Игрок 2 - ходит первым\r")
        return 1


def next_player(number_move):
    return 2 if number_move % 2 == 0 else 1


def redraw_field(cord_x, cord_y, next_board, symbol):
    print("Игровое поле:\r")
    next_board[int(cord_x)][int(cord_y)] = symbol
    for row in next_board:
        for x in row:
            print("{:4s}".format(x), end="")
        print()
    return next_board


def cell_is_empty_or_not(field, cord_x, cord_y):
    if field[int(cord_x)][int(cord_y)] != "-":
        print("Вы не можете пойти по этим координатам. Ечейка уже содержит игровой символ")
        return True
    else:
        return False


def no_wins(field):
    count = 0
    for row in field:
        for x in row:
            if x != "-":
                count += 1
    if count == 15:
        print("Ничья!\r")
    return True


def is_winner(field, symbol):
    if ((field[3][1] == "X" and field[3][2] == "X" and field[3][3] == "X") or
            (field[3][1] == "O" and field[3][2] == "O" and field[3][3] == "O")):
        if symbol == "X":
            print("Игрок, играющий X'ми - выйграл\r")
        if symbol == "O":
            print("Игрок, играющий O'ками - выйграл\r")
        return True
    if ((field[2][1] == "X" and field[2][2] == "X" and field[2][3] == "X") or
            (field[2][1] == "O" and field[2][2] == "O" and field[2][3] == "O")):
        if symbol == "X":
            print("Игрок, играющий X'ми - выйграл\r")
        if symbol == "O":
            print("Игрок, играющий O'ками - выйграл\r")
        return True
    if ((field[1][1] == "X" and field[1][2] == "X" and field[1][3] == "X") or
            (field[1][1] == "O" and field[1][2] == "O" and field[1][3] == "O")):
        if symbol == "X":
            print("Игрок, играющий X'ми - выйграл\r")
        if symbol == "O":
            print("Игрок, играющий O'ками - выйграл\r")
        return True
    if ((field[1][1] == "X" and field[2][2] == "X" and field[3][3] == "X") or
            (field[1][1] == "O" and field[2][2] == "O" and field[3][3]) == "O"):
        if symbol == "X":
            print("Игрок, играющий X'ми - выйграл\r")
        if symbol == "O":
            print("Игрок, играющий O'ками - выйграл\r")
        return True
    if ((field[1][3] == "X" and field[2][2] == "X" and field[3][1] == "X") or
            (field[1][3] == "O" and field[2][2] == "O" and field[3][1] == "O")):
        if symbol == "X":
            print("Игрок, играющий X'ми - выйграл\r")
        if symbol == "O":
            print("Игрок, играющий O'ками - выйграл\r")
        return True
    if ((field[1][1] == "X" and field[2][1] == "X" and field[3][1] == "X") or
            (field[1][1] == "O" and field[2][1] == "O" and field[3][1] == "O")):
        if symbol == "X":
            print("Игрок, играющий X'ми - выйграл\r")
        if symbol == "O":
            print("Игрок, играющий O'ками - выйграл\r")
        return True
    if ((field[1][2] == "X" and field[2][2] == "X" and field[3][2] == "X") or
            (field[1][2] == "O" and field[2][2] == "O" and field[3][2] == "O")):
        if symbol == "X":
            print("Игрок, играющий X'ми - выйграл\r")
        if symbol == "O":
            print("Игрок, играющий O'ками - выйграл\r")
        return True
    if ((field[1][3] == "X" and field[2][3] == "X" and field[3][3] == "X") or
            (field[1][3] == "O" and field[2][3] == "O" and field[3][3] == "O")):
        if symbol == "X":
            print("Игрок, играющий X'ками - выйграл\r")
        if symbol == "O":
            print("Игрок, играющий O'ками - выйграл\r")
        return True
    return False


print("Крестики-нолики\r")
who_f = who_first()
symbol_start = ask_figure()
is_win = False
no_win = False
moves = 1
print(f"\r\nИгрок {who_f + 1} выбрал {symbol_start}")
i = None
i = (2 if who_f == 0 else 1)
symbol_first, symbol_second = None, None
if symbol_start.upper() == "X" and i == 1:
    symbol_second = "X"
    symbol_first = "O"
    print(f"\r\nВторой игрок играет {symbol_first}")
if symbol_start.upper() == "O" and i == 1:
    symbol_second = "O"
    symbol_first = "X"
    print(f"\r\nВторой игрок играет {symbol_first}")
if symbol_start.upper() == "X" and i == 2:
    symbol_second = "O"
    symbol_first = "X"
    print(f"\r\nВторой игрок играет {symbol_second}")
if symbol_start.upper() == "O" and i == 2:
    symbol_second = "X"
    symbol_first = "O"
    print(f"\r\nВторой игрок играет {symbol_second}")
board = field_for_game()

while True:
    pos = ask_game_move()
    empty = cell_is_empty_or_not(board, pos[:1], pos[1:])
    while True:
        if empty:
            pos = ask_game_move()
            empty = cell_is_empty_or_not(board, pos[:1], pos[1:])
        else:
            break
    if moves == 9:
        no_win = no_wins(board)
        if no_win:
            if next_player(i) == 1:
                redraw_field(pos[:1], pos[1:], board, symbol_second.upper())
            if next_player(i) == 2:
                redraw_field(pos[:1], pos[1:], board, symbol_first.upper())
            break
    if next_player(i) == 1:
        board = redraw_field(pos[:1], pos[1:], board, symbol_second.upper())
        is_win = is_winner(board, symbol_second.upper())
        if is_win:
            break
        print("Следующий ход за игроком 1")
    if next_player(i) == 2:
        board = redraw_field(pos[:1], pos[1:], board, symbol_first.upper())
        is_win = is_winner(board, symbol_first.upper())
        if is_win:
            break
        print("Следующий ход за игроком 2")
    moves += 1
    i += 1
