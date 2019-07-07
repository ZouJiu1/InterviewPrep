import random

def paopao_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

x = [random.randint(0, 100) for i in range(10)]
print('before sorting', x)
r = paopao_sort(x)
print('after sorting', r)