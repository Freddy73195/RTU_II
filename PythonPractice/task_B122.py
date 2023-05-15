# Один из способов придумать пароль – взять фразу и оставить первые буквы
# каждого слова. Написать функцию make_password, выполняющую задачу генерации
# такого пароля из заданной фразы, при этом буквы i и I заменить на цифру 1,
# буквы o и O на цифру 0, буквы s и S на цифру 5.
#
# Примеры:
# make_password("The future belongs to those, Who believe in beauty of their dreams") ==> "TfbttWb1b0td"

import traceback
import string


def make_password(phrase):
    # Тело функции
    st = phrase
    print(st)
    a = st.split(' ')
    print(a)
    print(len(a))
    b = ''
    for i in range(len(a)):
        if (a[i][0] == 'i' or a[i][0] == 'I'):
            b += '1'
        elif (a[i][0] == 'o' or a[i][0] == 'O'):
            b += '0'
        elif (a[i][0] == 's' or a[i][0] == 'S'):
            b += '5'
        else:
            b += a[i][0]

    print(b)
    return b


# Тесты
try:
    assert make_password("Give me liberty or give me sweets") == "Gml0gm5"
    assert make_password("Keep Calm and Carry On") == "KCaC0"
    assert make_password("The future belongs to those, Who believe in beauty of their dreams") == "TfbttWb1b0td"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
