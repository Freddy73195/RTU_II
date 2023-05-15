# Написать функцию tic_tac_toe(board), которая получает состояние поля для игры в крестики-нолики и опредляет победителя. 
# Поле представлено в виде спсика 3x3, где значение равно 0 - точка пуста, 1 - это «X», или 2 - это «O».
# Функция должна возвращать: -1 если это ничья.
#
# Пример:
# tic_tac_toe([[1, 1, 1],
#              [0, 2, 2],
#              [0, 0, 0]]) ==> 1


import traceback


def tic_tac_toe(board):
    # Тело функции
    a = board

    if ((a[0][0]) == (a[1][0]) == (a[2][0]) == 1
    or (a[0][1]) == (a[1][1]) == (a[2][1]) == 1
    or (a[0][2]) == (a[1][2]) == (a[2][2]) == 1
    or (a[0][0]) == (a[0][1]) == (a[0][2]) == 1
    or (a[1][0]) == (a[1][1]) == (a[1][2]) == 1
    or (a[2][0]) == (a[2][1]) == (a[2][2]) == 1
    or (a[0][0]) == (a[1][1]) == (a[2][2]) == 1
    or (a[2][0]) == (a[1][1]) == (a[0][2]) == 1):
        print(a)
        b = 1
        return b
    if ((a[0][0]) == 0 or (a[1][0]) == 0 or (a[2][0]) == 0
    or (a[0][1]) == 0 or (a[1][1]) == 0 or (a[2][1]) == 0
    or (a[0][2]) == 0 or (a[1][2]) == 0 or (a[2][2]) == 0
    or (a[0][0]) == 0 or (a[0][1]) == 0 or (a[0][2]) == 0
    or (a[1][0]) == 0 or (a[1][1]) == 0 or (a[1][2]) == 0
    or (a[2][0]) == 0 or (a[2][1]) == 0 or (a[2][2]) == 0
    or (a[0][0]) == 0 or (a[1][1]) == 0 or (a[2][2]) == 0
    or (a[2][0]) == 0 or (a[1][1]) == 0 or (a[0][2]) == 0):
        print(a)
        b = 0
        return b
    elif ((a[0][0]) == (a[1][0]) == (a[2][0]) == 2
    or (a[0][1]) == (a[1][1]) == (a[2][1]) == 2
    or (a[0][2]) == (a[1][2]) == (a[2][2]) == 2
    or (a[0][0]) == (a[0][1]) == (a[0][2]) == 2
    or (a[1][0]) == (a[1][1]) == (a[1][2]) == 2
    or (a[2][0]) == (a[2][1]) == (a[2][2]) == 2
    or (a[0][0]) == (a[1][1]) == (a[2][2]) == 2
    or (a[2][0]) == (a[1][1]) == (a[0][2]) == 2):
        print(a)
        b = 2
        return b
    else:
        print(a)
        b = -1
        return b

# Тесты
try:
    board1 = [[0, 0, 1],
            [0, 1, 2],
            [2, 1, 0]]
    # assert tic_tac_toe(board1) == -1
    assert tic_tac_toe(board1) == 0
    board2 = [[1, 1, 1],
            [0, 2, 2],
            [0, 0, 0]]
    assert tic_tac_toe(board2) == 1
    board3 = [[1, 2, 1],
            [1, 2, 2],
            [2, 2, 1]]
    assert tic_tac_toe(board3) == 2
    board4 = [[2, 1, 2],
            [2, 1, 1],
            [1, 2, 1]]
    # assert tic_tac_toe(board4) == 0
    assert tic_tac_toe(board4) == -1
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")