import time
import random

a = []
n = int(input())
for i in range(n):
    a.append(random.randint(1, 20))


print(a)
count1 = 0
count2 = 0

def mergeSort(alist):
    global count1, count2

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            count1 += 1
            if lefthalf[i]<righthalf[j]:
                count2 += 1
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                count2 += 1
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            count2 += 1
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            count2 += 1
            j=j+1
            k=k+1


start = time.time()
mergeSort(a)
end = time.time()
total = end - start
print(a)
print(f'Программа выполнилась за { "%.4f" %total}')
print(f'Программа делала сранение {count1}')
print(f'Программа перемещала элементы  {count2}')
