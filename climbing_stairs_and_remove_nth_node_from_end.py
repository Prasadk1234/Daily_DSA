# climbing_tress
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        f, s = 1, 2

        for i in range(3, (n + 1)):
            t = f + s
            f = s
            s = t

        return s

#remove nth node from end
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        res = ListNode(0)
        res.next = head

        first = res
        second = res

        for i in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return res.next

#genrate parenthesis
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output = []

        def par(l, r, stack, cand):

            if l == r == 0:
                output.append(cand)
                return
            if l > 0:
                par(l - 1, r, stack + 1, cand + "(")
            if r > 0 and stack > 0:
                par(l, r - 1, stack - 1, cand + ")")

        par(n, n, 0, "")

        return output
