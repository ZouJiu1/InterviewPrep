from sort.QuickSort import quicksort
import random
import time

class search_median(object):
    def __init__(self, array, way):
        self.array = array
        self.medi = None
        self.ok = False
        self.save = []
        self.way = way

    def median(self, left, right):
        if self.way == 1:
            self.quicksort1(self.array, left, right)
        else:
            self.quicksort2(self.array, left, right)
            if len(self.save)==1:
                self.medi = round((self.array[self.length//2] + self.array[self.length//2-1])/2, 1)

    def quicksort1(self, part, left, right):
        self.length = len(self.array)
        if (left == right) and (left == self.length // 2):
            self.medi = self.array[left]
            return
        if left < right:
            sholdindex = self.partition(part, left, right)
            if (sholdindex == self.length // 2):
                self.medi = self.array[sholdindex]
                return
            if (sholdindex > self.length // 2):
                self.quicksort1(part, left, sholdindex - 1)
            elif (sholdindex < self.length // 2):
                self.quicksort1(part, sholdindex + 1, right)

    def quicksort2(self, part, left, right):
        self.length = len(self.array)
        if ((left == right) and (left == self.length // 2)) or ((left == right) and (left == self.length // 2 - 1)):
            self.save.append(self.array[left])
            if len(self.save) == 2:
                self.medi = round((self.save[0] + self.save[1]) / 2, 1)
                return
        if left < right:
            sholdindex = self.partition(part, left, right)
            if (sholdindex == self.length // 2) or (sholdindex == self.length // 2 - 1):
                self.save.append(self.array[sholdindex])
                if len(self.save) == 2:
                    self.medi = round((self.save[0] + self.save[1]) / 2, 1)
                    return
            if (sholdindex > self.length // 2):
                self.quicksort2(part, left, sholdindex - 1)
            elif (sholdindex < self.length // 2):
                self.quicksort2(part, sholdindex + 1, right)
            else:
                self.quicksort2(part, left, sholdindex - 1)
                self.quicksort2(part, sholdindex + 1, right)

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
    obj = search_median(x_copy, 1)
    obj.median(0,len(x_copy)-1)
    # res = search_median(x).median(0,len(x)-1)
    print('使用快速排序的过程找到的中位数是：', obj.medi, '用时为：',time.time()-s2)