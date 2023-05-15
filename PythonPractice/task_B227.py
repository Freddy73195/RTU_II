# Написать функцию longest_word, которая возвращает последнее наибольшее по длине слово из заданной строки
#
# Пример:
# longest_word("red blue gold") ==> "gold"


import traceback


def longest_word(string_of_words):
    sow = string_of_words
    print(sow)
    a = sow.split(' ')
    print(a)
    b = a[0][::]
    print(b)
    for i in range(len(a) - 1):
        if (len(a[i + 1][::]) > len(b)):
            b = a[i + 1][::]
        if (len(a[i + 1][::]) == len(b)):
            b = a[i + 1][::]
        print(b)
    return b


# Тесты
try:
    assert longest_word("a b c d e fgh") == "fgh"
    assert longest_word("one two three four five") == "three"
    assert longest_word("red blue grey") == "grey"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
