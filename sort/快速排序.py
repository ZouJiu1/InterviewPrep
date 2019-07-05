import random

class quicksort(object):
    def __init__(self, array):
        self.array=array
        self.start = 0
        self.end = len(array)-1
    def partition(self, part, start, end):
        shold = part[start]
        temp =start
        while start < end:
            while (start < end) and (part[end] >= shold):
                end = end - 1
            while (start < end) and (part[start] <= shold):
                start = start + 1
            if start<end:
                part[start], part[end] = part[end], part[start]
                start += 1
                end = end-1
        part[temp] = part[start]
        part[start] = shold
        return start

    def quicksorts(self, array, start, end):
        if start<end:
            sholdindex=self.partition(array, start, end)
            self.quicksorts(array, start, sholdindex-1)
            self.quicksorts(array, sholdindex+1, end)
        return array

    def qsort(self):
        return self.quicksorts(self.array, self.start, self.end)

x = [1,0,100,6]#[random.randint(0,19) for i in range(10)]
print(x)
r=quicksort(x).qsort()
print(r)