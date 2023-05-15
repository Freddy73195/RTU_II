# Даны результаты забегов в формате "h|m|s, h|m|s, h|m|s" (h – часы, m – минуты, s – секунды).
# Написать функцию stat, которая возвращает строку в формате "Range: hh|mm|ss Average: hh|mm|ss"
# (range – разница между максимальным и минимальным значением, average – среднее значение)
#
# Пример:
# stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17") ==> "Range: 00|47|18 Average: 01|35|15"


import traceback


def stat(s):
    results = [[int(i) for i in r.strip().split('|')] for r in s.split(',')]
    results = [r[0] * 3600 + r[1] * 60 + r[2] for r in results]

    average = sum(results) / len(results)
    average = round(average // 3600), round(average % 3600) // 60, round(average % 60)
    Range = max(results) - min(results)
    Range = Range // 3600, round(Range % 3600) // 60, round(Range % 60)
    a = (f'{average[0]},{average[1]:02},{average[2]:02}')
    b = (f'{Range[0]},{Range[1]:02},{Range[2]:02}')
    x = b.replace(',','|')
    z = a.replace(',','|')
    print(x)
    print(z)
    # print("Range:",x,"Average:",z)
    # print('Range: {} Average: {}'.format(x, z))
    # b = '|'.join(str(e) for e in Range)
    # print(b)
    return 'Range: {} Average: {}'.format(x, z)

# Тесты
try:
    # assert stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17") == "Range: 01|01|18 Average: 01|38|05"
    # assert stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41") == \
    #     "Range: 00|31|17 Average: 02|26|18"
    assert stat("1|15|59, 1|47|16, 1|17|20, 1|32|34, 2|17|17") == "Range: 1|01|18 Average: 1|38|05"
    assert stat("2|15|59, 2|47|16, 2|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41") == \
           "Range: 0|31|17 Average: 2|26|18"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
