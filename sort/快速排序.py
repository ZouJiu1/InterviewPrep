import random

class quicksort(object):
    def __init__(self, array, way):
        self.array = array
        self.left = 1
        self.right = len(array)-1
        self.way = way

    def partition1(self, part, left, right):
        shold = part[left]
        temp =left
        while left < right:
            while (left < right) and (part[right] >= shold):
                right = right - 1
            part[left]=part[right]
            while (left < right) and (part[left] <= shold):
                left = left + 1
            part[right]=part[left]
            # if left<right:
            #     part[left], part[right] = part[right], part[left]
        # part[temp] = part[left]
        part[left] = shold
        return left

    def quicksorts(self, array, left, right):
        if left<right:
            sholdindex=self.partition1(array, left, right)
            self.quicksorts(array, left, sholdindex-1)
            self.quicksorts(array, sholdindex+1, right)
        return array

    def qsort(self):
        if self.way == 1:
            return self.quicksorts(self.array, 0, len(self.array)-1)
        else:
            return self.quicksorts()

x = [random.randint(0,19) for i in range(10)]
print(x)
r=quicksort(x,1).qsort()
print(r)