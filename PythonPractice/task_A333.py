# Написать функцию кодирования encode(message, key)
# Процесс шифрования: каждой букве латинского алфавита abcdefghijklmnopqrstuvwxyz
# последовательно ставится в соответствие число от 1 до 26.
# Дальше к каждому числу последовательно прибавляется цифры из ключа.
#
# Пример:
# слово: abcxyz, код: 4567 =>
# [a->1, b->2, c->3, x->24, y->25, z->26] =>
# [1 + 4, 2 + 5, 3 + 6, 24 + 7, 25 + 4, 26 + 5] => код: [5, 7, 8, 31, 29, 31]


import traceback
import string
from array import *
import numpy as zxc

def encode(message, key):
    # Тело функции
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    a = list(message)
    c = list()
    # print(len(a))
    for i in range(len(a)):
        c.append(values[a[i]])
        # print(c)
    # b = values[a[0]]
    m_z = zxc.asarray(c, dtype=zxc.int64)
    # print(m_z)
    b = list(str(key))
    key_z = zxc.asarray(b, dtype=zxc.int64)
    # print(key_z)
    d = array('i', [0])
    cou = 0
    for i in range(len(a)):
        d.append(m_z[i] + key_z[cou])
        cou += 1
        if (len(key_z) <= cou):
            cou = 0
    # print(d)
    d.pop(0)
    # print(d)
    d = list(d)
    print(d)
    return d

# Тесты
try:
    assert encode("scout", 1939) == [20, 12, 18, 30, 21]
    assert encode("masterpiece", 1939) == [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")


    # a = list(message)
    # print(a)
    # b = str(key)
    # c = list(b)
    # print(c)
    # d = len(a)
    # print(d)
    # e = list
    # f = 0
    # print(a[f])
    # print(c[f])
    # print(values[a[f]] + c[f])
    # for i in range (d):
    #     e.append(values[a[f]] + c[f])
    #     f += 1
    # return e