# class Solution:
#     def longestPalindrome(self, s):
#         if len(s) <= 1:
#             return s
#         result = {}
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 substring = s[i:j]
#                 rs = substring[::-1]
#                 if substring == rs:
#                     result[substring] = len(rs)
#         r = sorted(result.items(),key=lambda x:x[1], reverse=True)
#         return r[0][0]

class Solution:
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        size = len(s)
        dp = [[False for _ in range(size)] for _ in range(size)]
        longest_1 = 1
        res = s[0]
        for r in range(1, size):
            for l in range(r):
                if s[l]==s[r] and (r-l<=2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    cur_len=r-l+1
                    if cur_len>longest_1:
                        longest_1=cur_len
                        res=s[l:r+1]
        return res

string = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
# string = "babad"
s = Solution()
r=s.longestPalindrome(string)
print(r)

