#encoding = utf-8
class Solution:
    # def isMatch(self, s, p):
    #     memo = dict()
    #     def dp(i, j):
    #         if (i, j) in memo:
    #             return memo[(i, j)]
    #         if j == len(p):
    #             return i == len(s)
    #         first = i < len(s) and p[j] in {s[i], '.'}
    #         if j <= len(p) - 2 and p[j + 1] == '*':
    #             ans = dp(i, j + 2) or first and dp(i + 1, j)
    #         else:
    #             ans = first and dp(i + 1, j + 1)
    #         memo[(i, j)] = ans
    #         return ans
    #     return dp(0, 0)

    # def isMatch(self, s, p):
    #     if not p:
    #         return not s
    #
    #     first = bool(s) and p[0] in [s[0], '.']
    #
    #     if len(p) >= 2 and p[1] == '*':
    #         return self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))
    #     else:
    #         return first and self.isMatch(s[1:], p[1:])
    def isMath(self, s, p):


st = 'aa'
p = 'a*'
solution = Solution()
r = solution.isMatch(st, p)
print(r)

