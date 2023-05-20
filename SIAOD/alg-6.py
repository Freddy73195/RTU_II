t = input()
# Алгоритм Бойера-Мура-Хорспула | Алгоритмы на Python
# https://bookflow.ru/algoritmy-i-struktury-dannyh-na-python/#%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9A%D0%BD%D1%83%D1%82%D0%B0-%D0%9C%D0%BE%D1%80%D1%80%D0%B8%D1%81%D0%B0-%D0%9F%D1%80%D0%B0%D1%82%D1%82%D0%B0_%D0%9A%D0%9C%D0%9F-%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B_%D0%BD%D0%B0_Python
S = set()  # уникальные символы в образе
M = len(t) # число символов в образе
d = {}     # словарь смещений
count1 = 0
count2 = 0
for i in range(M-2, -1, -1): # итерации с предпоследнего символа
    count1 += 1
    if t[i] not in S: # если символ еще не добавлен в таблицу
        d[t[i]] = M-i-1
        count2 += 1
        S.add(t[i])
count1 += 1
if t[M-1] not in S:  # отдельно формируем последний символ
    count2 += 1
    d[t[M-1]] = M
d['*'] = M   # смещения для прочих символов
a = open("text.txt").readlines()
print(a[0])
a = a[0]
N = len(a)
if N >= M:
    i = M-1  # счетчик проверяемого символа в строке
    while(i < N):
        k = 0
        j = 0
        flBreak = False
        for j in range(M-1, -1, -1):
            count1 +=1
            if a[i-k] != t[j]:
                count1 += 1
                if j == M-1:
                    count2 += 1
                    off = d[a[i]] if d.get(a[i], False) else d['*'] # смещение, если не равен последний символ образа
                else:
                    count2 += 1
                    off = d[t[j]] # смещение, если не равен не последний символ образа
                i += off # смещение счетчика строки
                flBreak = True  # если несовпадение символа, то flBreak = True
                break
            k += 1 # смещение для сравниваемого символа в строке
        if not flBreak: # если дошли до начала образа, значит, все его символы совпали
            print(f"образ найден по индексу {i-k+1}")
            print(count1, count2)
            print(len(a) + len(t))
            break
    else:
        print("образ не найден")
else:
    print("образ не найден")