# Задан список положительных чисел arr и положительное число k.
# Написать функцию minimum_steps, которая определяет сколько наименьших элементов списка
# в порядке возрастания нужно сложить, чтобы их сумма была больше или равна числу k
#
# Пример:
# minimum_steps([4,6,3], 7) ==> 2


import traceback


def minimum_steps(arr, k):
    arr.sort()
    print(arr)
    a = 0
    b = 0
    c = 0
    while (a < k):
        a = a + arr[b]
        b = b + 1
        c = c + 1
    print(c)
    return c


# Тесты
try:
    assert minimum_steps([8,9,10,4,2], 23) == 4
    assert minimum_steps([19,98,69,28,75,45,17,98,67], 464) == 9
    assert minimum_steps([10,9,9,8], 17) == 2
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")