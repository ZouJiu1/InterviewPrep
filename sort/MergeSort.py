import random
import time

class MergeSort(object):
    def __init__(self, array):
        self.array = array
        self.length = len(self.array)

    def merge_sort(self, array, L, R):
        if (L==R):
            return
        else:
            #取中间的数
            M = (L+R)//2
            #左边的数不断进行划分
            self.merge_sort(array, L, M)
            #右边的数不断进行划分
            self.merge_sort(array, M+1, R)
            self.merge(array, L, M+1, R)

    def merge(self, array, L, M_, R):
        left_len = M_ - L
        right_len = R - M_+1

        left = array[L : M_]
        right = array[M_:R+1]
        i=0
        j=0
        k=L
        while (i < left_len) and (j < right_len):
            if (left[i] < right[j]):
                self.array[k] = left[i]
                i += 1
                k += 1
            else:
                self.array[k] = right[j]
                j += 1
                k += 1

        #由于两个合并的数组都是已经排好序的数组，所以数组内部不需要重新排序
        #递归的最底端是两个数的排序

        #左端和右端不可能同时剩余有数，只可能是一端剩余有数
        while (i<left_len):   #左端有剩余的数，都是两个数组中的较大的数
            self.array[k] = left[i]
            i += 1
            k += 1
        while (j<right_len): #右端有剩余的数，是较大的数
            self.array[k] = right[j]
            j +=1
            k +=1

if __name__=='__main__':
    compare = True
    if compare:
        s=time.time()
        x = [random.randint(0, 1000000000) for i in range(10000000)]
        print('before sorting', x[:10])
        for i in range(10):
            ms = MergeSort(x)
            ms.merge_sort(x, 0, len(x) - 1)
            print('after sorting %d'%(i+1), ms.array[:10])
        print('used time is: ', round((time.time() - s)/10, 4), 's')
    else:
        s=time.time()
        x = [random.randint(0, 100) for i in range(10)]
        print('before sorting', x)
        ms = MergeSort(x)
        ms.merge_sort(x, 0, len(x)-1)
        print('after sorting', ms.array, 'used time: ', round((time.time() - s)/10, 4))