# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         if len(s)==0:
#             return 0
#         start = s[0]
#         res = []
#         for i in range(len(s)-1):
#             if (s[i+1] != s[i]) and (s[i+1] not in start):
#                 start += s[i]
#                 if ((i + 1) == len(s) - 1) or (i==0):
#                     start += s[i + 1]
#                 else:
#                     start += s[i]
#             else:
#                 res.append(len(start))
#                 start = s[i]
#         res.append(len(start))
#         if len(res)==0:
#             return 1
#         return max(res)

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         if len(s) <= 1:
#             return len(s)
#         start = ''
#         res = []
#         for j in range(len(s)):
#             if s[j] not in start:
#                 start += s[j]
#             else:
#                 temp = start.index(s[j])
#                 res.append(len(start))
#                 start = start[temp+1:]+s[j]
#                 if j == len(s) - 1:
#                     return max(res)
#             if (start!=''):
#                 res.append(len(start))
#             if j==len(s)-1:
#                 return max(res)

class Solution:
    def lengthOfLongestSubstring(self, s):
        dic = {}
        left = 0
        length = 0
        for i in range(len(s)):
            if (s[i] not in dic.keys()) or (dic[s[i]] < left):
                length = max(length, i - left + 1)
            else:
                left = dic[s[i]]
            dic[s[i]] = i + 1
        return length

string = "tmmzuxt"
s = Solution()
r = s.lengthOfLongestSubstring(string)
print(r)
