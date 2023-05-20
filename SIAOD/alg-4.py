from random import randint
import time
count1 = 0
count2 = 0
def fun(mas,num,l):
    global count1
    i = 0
    mas.append(num)
    while True:
        if num == mas[i]:

            print(mas[i])
            if i == len(mas) - 1:
                count1 += 1
                print("None...")
                break
            else:
                count1 += 1
                print(i)
                break
        count1 +=1
        i += 1
    print(mas)
    print(f'Программа делала сранение {count1}')
a = []
l = int(input())
for i in range(l+1):
    a.append(randint(1, 100))
print(a)
num = int(input())
fun(a,num,l)



