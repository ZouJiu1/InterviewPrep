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
            print(self.save, self.medi, self.array)
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

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = nums1+nums2
        if len(x)%2==0:
            r = search_median(x, 2)
        else:
            r = search_median(x, 1)
        r.median(0, len(x) - 1)
        return r.medi

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x = nums1+nums2
        x.sort()
        length = len(x)
        if len(x)%2==0:
            return float((x[length//2]+x[length//2-1]))/2
        else:
            return float(x[length])

x1 = [1, 2]
x2 = [3, 4]
s=Solution()
s=s.findMedianSortedArrays(x1, x2)
print(s)
