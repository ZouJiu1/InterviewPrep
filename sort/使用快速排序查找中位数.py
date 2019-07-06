from sort.QuickSort import quicksort
import random
import time

class search_median(object):
    def __init__(self, array):
        self.array = array
        self.medi = None
        self.ok=False

    def median(self, left, right):
        self.quicksort(self.array, left, right)

    def quicksort(self, part, left, right):
        self.length = len(self.array)
        if  self.ok:
            return
        if left < right:
            sholdindex = self.partition(part, left, right)
            if (sholdindex == self.length//2):
                self.ok=True
                self.medi=self.array[sholdindex]
            if (sholdindex > self.length//2):
                self.quicksort(part, left, sholdindex - 1)
            elif (sholdindex < self.length//2):
                self.quicksort(part, sholdindex + 1, right)

    def partition(self, part, left, right):
        shold = part[left]
        temp = left
        while left < right:
            while (left < right) and (part[right] >= shold):
                right = right - 1
            while (left < right) and (part[left] <= shold):
                left = left + 1
            if left < right:
                part[left], part[right] = part[right], part[left]
        part[temp] = part[left]
        part[left] = shold
        return left

if __name__=="__main__":
    #先排序，然后取中间的数
    s1=time.time()
    x = [random.randint(0, 100000) for i in range(10000)]
    x_copy = x.copy()
    print('before sorting',  x[:19])
    r = quicksort(x).qsort(2)
    print('after sorting',  x[:19])
    print('先排序，然后找到的中位数是：', r[len(x)//2],'用时为：',time.time()-s1)

    #在快速排序的过程中找到中位数
    s2=time.time()
    obj = search_median(x_copy)
    obj.median(0,len(x_copy)-1)
    # res = search_median(x).median(0,len(x)-1)
    print('使用快速排序的过程找到的中位数是：', obj.medi, '用时为：',time.time()-s2)