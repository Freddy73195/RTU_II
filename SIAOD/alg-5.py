import random
a = [random.randint(0,100) for _ in range(int(input()))]
count = 0
a.sort()
print(a)

key = int(input())
while len(a) > 2:
    center = len(a) // 2
    if(a[center] > key):
        a = a[0:center]

    elif(a[center] <= key):
        a = a[center:]
    count += 1
    print(a)
if key not in a:
    print(f'Число {key} нет в списке')
else:
    print(f'Число {key} есть в списке')
    for i in range(len(a)):
        if a[i] == key:
            print(i)
print(count)

