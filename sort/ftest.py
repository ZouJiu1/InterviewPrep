def quicksort(ar, p, r):
    if p < r:
        q = partition(ar, p, r)
        arr[p], arr[q] = ar[q], arr[p]
        quicksort(ar, p, q - 1)
        quicksort(ar, q + 1, r)
    else:
        return


def partition(ar, p, r):
    x = ar[p]
    i = p
    j = r
    while 1:
        while ar[j] > x:
            j = j - 1
        while ar[i] < x:
            i = i + 1
        if i < j:
            ar[i], ar[j] = ar[j], ar[i]
        else:
            return j


arr = [1,0,100,6]
import numpy as np

np.sort()
print("initial array:\n", arr)
quicksort(arr, 0, len(arr) - 1)
print("result array:\n", arr)