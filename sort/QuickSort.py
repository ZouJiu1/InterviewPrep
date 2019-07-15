#encoding=utf-8
#其中速度最快的是第六种方法
import random
import time
import matplotlib.pyplot as plt
import numpy as np

class quicksort(object):
    def __init__(self, array):
        self.array = array
        self.left = 1
        self.right = len(array)-1

    def rand_choose(self, left, right):
        return random.randrange(left, right+1, 1)

    def partition1(self, part, left, right):
        '''
        每进行到节点就补全，其中part[left]已经赋值给shold
        使用>=的原因是单独使用>，如果和基准元素相等，会陷入循环中
        '''
        shold = part[left]
        while left < right:
            while (left < right) and (part[right] >= shold):
                right = right - 1
            part[left]=part[right]
            while (left < right) and (part[left] <= shold):
                left = left + 1
            part[right]=part[left]
        part[left] = shold
        return left

    def partition2(self, part, left, right):
        '''
        交换大小不等的数对，双指针交换，最左侧为枢纽值
        '''
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

    def partition3(self, part, left, right):
        '''
        交换大小不等的数对，双指针交换，最右侧为枢纽值
        '''
        shold = part[right]
        temp = right
        while left < right:
            while (left < right) and (part[left] <= shold):
                left = left + 1
            while (left < right) and (part[right] >= shold):
                right = right - 1
            if left<right:
                part[left], part[right] = part[right], part[left]
        part[temp] = part[left]
        part[left] = shold
        return left

    def partition4(self, part, left, right):
        #双指针单向划分
        low = left-1
        shold = part[right]
        for high in range(left, right):
            if part[high] <= shold:
                low=low+1
                if low != high:
                    part[low],part[high]=part[high], part[low]
        part[right], part[low+1]=part[low+1], shold
        return low+1

    def partition5(self, part, left, right):
        #随机选取枢纽值方法
        index=self.rand_choose(left,right)
        part[index], part[left] = part[left], part[index]
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

    def median(self,part, left,right):
        center = (left+right)//2
        if part[left]>part[center]:
            part[left],part[center]=part[center],part[left]
        if part[left]>part[right]:
            part[left],part[right]=part[right],part[left]
        if part[right]<part[center]:
            part[right],part[center]=part[center],part[right]
        part[center],part[right-1]=part[right-1],part[center]
        return part

    def insertSort(self, part, left, right):
        for i in range(left+1,right+1):
            temp=part[i]
            for j in range(i,left-1,-1):
                if temp<part[j-1]:
                    part[j]=part[j-1]
                else:
                    break
            part[j] = temp

    def partition6(self, part, left, right):
        #三数取中法，并在子序列长度小于10时，使用直接插入排序
        if (left + 8 < right):
            part = self.median(part,left,right)
            part[right-1], part[left] = part[left], part[right-1]
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
        else:
            self.insertSort(part,left,right)
            return left

    def quicksorts(self, array, left, right, way):
        if left<right:
            if way==1:
                sholdindex=self.partition1(array, left, right)
            elif way==2:
                sholdindex=self.partition2(array, left, right)
            elif way==3:
                sholdindex=self.partition3(array, left, right)
            elif way==4:
                sholdindex=self.partition4(array,left,right)
            elif way==5:
                sholdindex=self.partition5(array,left,right)
            elif way==6:
                sholdindex=self.partition6(array,left,right)
            self.quicksorts(array, left, sholdindex-1, way=way)
            self.quicksorts(array, sholdindex+1, right, way=way)
        return array

    def qsort(self,way):
        return self.quicksorts(self.array, 0, len(self.array)-1, way)

if __name__=='__main__':
    #参考https://blog.csdn.net/u013074465/article/details/42083607/
    compare=True
    if compare:
        x_ = [random.randint(0, 1000000000) for i in range(10000000)]
        x = x_.copy()
        times = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        for i in range(10):
            print('poch %d---------------------------------------------------------------------' % (i + 1))
            s1 = time.time()
            r = quicksort(x_.copy()).qsort(1)
            print('way 1: ', r[:100])
            times[1].append(time.time() - s1)
            print('way 1 used time: ', round(time.time() - s1, 4))

            s2 = time.time()
            r = quicksort(x_.copy()).qsort(2)
            print('way 2: ', r[:100])
            times[2].append(time.time() - s2)
            print('way 2 used time: ', round(time.time() - s2, 4))

            s3 = time.time()
            r = quicksort(x_.copy()).qsort(3)
            print('way 3: ', r[:100])
            times[3].append(time.time() - s3)
            print('way 3 used time: ', round(time.time() - s3, 4))

            s4 = time.time()
            r = quicksort(x_.copy()).qsort(4)
            print('way 4: ', r[:100])
            times[4].append(time.time() - s4)
            print('way 4 used time: ', round(time.time() - s4, 4))

            s5 = time.time()
            r = quicksort(x_.copy()).qsort(5)
            print('way 5: ', r[:100])
            times[5].append(time.time() - s5)
            print('way 5 used time: ', round(time.time() - s5, 4))

            s6 = time.time()
            r = quicksort(x_.copy()).qsort(6)
            print('way 6: ', r[:100])
            times[6].append(time.time() - s6)
            print('way 6 used time: ', round(time.time() - s6, 4))

        res = []
        times = sorted(times.items(), key=lambda x: x[0])
        print(times)
        for j in times:
            res.append(np.mean(j[1]))

        fig = plt.figure(figsize=(6, 7))
        plt.plot([1, 2, 3, 4, 5, 6], res)
        plt.xlabel('way')
        plt.ylabel('time/s')
        plt.savefig(r'quicksort_compare_time.png')
        plt.show()

    else:
        x = [random.randint(0,10) for i in range(10)]
        print('before sorting',x)
        r=quicksort(x).qsort(6)
        print('after sorting',r)
