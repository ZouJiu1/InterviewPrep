class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, j in enumerate(nums):
            if (nums[i] == target//2) and (target//2 in dic.keys()):
                return [dic[j], i]
            dic[j] = i
            if ((target-j) in dic.keys()) and (dic[target-j]!=i):
                return [dic[target-j],i]
        return []

s=Solution()
r=s.twoSum([1,6,7,9],7)
print(r)
