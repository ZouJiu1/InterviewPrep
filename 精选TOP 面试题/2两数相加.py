# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         i1 = 1
#         s1 = 0
#         while l1.next != None:
#             s1 += l1.val*i1
#             i1 = 10*i1
#             l1 = l1.next
#         s1 += l1.val*i1
#
#         i2=1
#         s2=0
#         while l2.next != None:
#             s2 += l2.val*i2
#             i2 = 10*i2
#             l2 = l2.next
#         s2 += l2.val*i2
#         result = 0
#         sts = str(s1+s2)
#         for i in range(len(sts)-1, -1, -1):
#             if result == 0:
#                 result = ListNode(sts[i])
#             else:
#                 line = [result]
#                 x = line.pop(0)
#                 while x.next!=None:
#                     line.append(x.next)
#                     x=line.pop(0)
#                 x.next=ListNode(sts[i])
#         return result
#
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         x1 = []
#         x2 = []
#         while (l1.next != None):
#             x1.append(l1.val)
#             l1 = l1.next
#         x1.append(l1.val)
#         while (l2.next != None):
#             x2.append(l2.val)
#             l2 = l2.next
#         x2.append(l2.val)
#
#         while len(x1) > len(x2):
#             x2 = x2 +[0]
#         while len(x1) < len(x2):
#             x1 = x1 +[0]
#         result = 0
#         pre=0
#         for i in range(len(x1)):
#             xs = x1[i] + x2[i] + pre
#             pre = 0
#             mod = 0
#             if (xs >= 10):
#                 mod = xs % 10
#                 xs = xs // 10 + pre
#                 if xs >= 1:
#                     pre = 1
#                     xs = 0
#             if result == 0:
#                 result = ListNode(xs + mod)
#                 if (pre == 1) and (len(x1) == 1):
#                     result.next = ListNode(1)
#             else:
#                 line = [result]
#                 x = line.pop(0)
#                 while x.next != None:
#                     line.append(x.next)
#                     x = line.pop(0)
#                 x.next = ListNode(xs + mod)
#                 if (pre == 1) and (i==len(x1)-1):
#                     x.next.next = ListNode(1)
#
#         return result

class Solution:
    def addTwoNumbers(self, l1, l2):
        p1=l1
        p2=l2
        pre=0
        first = ListNode(0)
        curr = first
        while(p1 != None) or (p2 != None):
            if p1==None:
                x=0
            else:
                x=p1.val
                p1=p1.next
            if p2==None:
                y=0
            else:
                y=p2.val
                p2=p2.next
            sum = x+y+pre
            mod = sum%10
            pre = sum//10
            curr.next=ListNode(mod)
            curr=curr.next
        if pre==1:
            curr.next=ListNode(1)
        return first.next


l1 = ListNode(8)
l1.next = ListNode(6)
# l1.next.next = ListNode(3)

l2 = ListNode(6)
l2.next = ListNode(4)
l2.next.next = ListNode(8)

s = Solution()
r = s.addTwoNumbers(l1, l2)
while r.next!=None:
    print(r.val)
    r=r.next
print(r.val)