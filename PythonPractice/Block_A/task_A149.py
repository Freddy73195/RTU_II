# Напишите функцию number_of_squares(limit), которая будет возвращать, сколько целых (начиная с 1, 2 ...) чисел, 
# возведенных в степень 2, а затем суммированных, меньше некоторого заданного числа в качестве параметра limit.
#
# Примеры:
# number_of_squares(6) => 2 -> 1 ^ 2 + 2 ^ 2 = 1 + 4 = 5 и 5 < 6
# number_of_squares(15) => 3 -> 1 ^ 2 + 2 ^ 2 + 3 ^ 2 = 1 + 4 + 9 = 14 и 14 < 15 


import traceback


def number_of_squares(limit):
#    c = 0
#   a = 1
#    b = 1
#    while (a < limit):
#       a = (b ** 2) + ((b + 1) ** 2)
#        b += 1
#       c += 1
#    print(c)
#   return c
    c = 0
    a = 0
    while a < limit:
        c += 1
        a += c**2
    print(c - 1)
    return c - 1


# Тесты
try:
    assert number_of_squares(1) == 0
    assert number_of_squares(2) == 1
    assert number_of_squares(5) == 1
    assert number_of_squares(6) == 2
    assert number_of_squares(15) == 3
    assert number_of_squares(100) == 6
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")