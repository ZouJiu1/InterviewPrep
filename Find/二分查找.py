from sort.QuickSort import quicksort

def split_find(arr,find):
    lindex = 0
    rindex = len(arr)
    while (lindex<=rindex):
        temp=(lindex+rindex)//2
        if arr[temp] == find:
            return temp
        elif arr[temp]<find:
            lindex = temp+1
        else:
            rindex = temp-1
    return -1

x = [1, 10, 9, 6, 7, 100, 4, 2, 16, 19, 21, 17, 12, 11, 6]
print('len(x) = ', len(x))

sort_x = quicksort(x).qsort(6)
print(sort_x)
r = split_find(sort_x, 16)
print(r, x[r])