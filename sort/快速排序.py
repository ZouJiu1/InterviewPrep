import random
class quicksort(object):
    def __init__(self, array, way):
        self.array = array
        self.left = 1
        self.right = len(array)-1
        self.way = way

    def rand_choose(self, left, right):
        random.randrange(left, right, 1)

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
        交换大小不等的数对，双指针交换
        '''
        shold = part[left]
        temp =left
        while left < right:
            while (left < right) and (part[right] >= shold):
                right = right - 1
            while (left < right) and (part[left] <= shold):
                left = left + 1
            if left<right:
                part[left], part[right] = part[right], part[left]
        part[temp] = part[left]
        part[left] = shold
        return left

    def partition3(self, part, left, right):
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

    def partition4(self, part, left, right):
        #随机选取枢纽值方法
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
    def quicksorts(self, array, left, right):
        if left<right:
            if self.way==1:
                sholdindex=self.partition1(array, left, right)
            elif self.way==2:
                sholdindex=self.partition2(array, left, right)
            elif self.way==3:
                sholdindex=self.partition3(array, left, right)
            # elif self.way==4
            self.quicksorts(array, left, sholdindex-1)
            self.quicksorts(array, sholdindex+1, right)
        return array

    def qsort(self):
        return self.quicksorts(self.array, 0, len(self.array)-1)

if __name__=='__main__':
    #参考https://blog.csdn.net/u013074465/article/details/42083607/
    x = [random.randint(0,19) for i in range(10)]
    print(x)
    r=quicksort(x, 3).qsort()
    print(r)