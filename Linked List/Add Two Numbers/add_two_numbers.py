# Leetcode 2 - Add Two Numbers
# Time: O(max(n, m))
# Space: O(max(n, m))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy
        carry = 0

        while l1 and l2:
            _sum = l1.val + l2.val + carry
            result.next = ListNode(_sum % 10)
            carry = _sum // 10
            result = result.next
            l1, l2 = l1.next, l2.next

        while l1:
            _sum = l1.val + carry
            result.next = ListNode(_sum % 10)
            carry = _sum // 10
            result = result.next
            l1 = l1.next

        while l2:
            _sum = l2.val + carry
            result.next = ListNode(_sum % 10)
            carry = _sum // 10
            result = result.next
            l2 = l2.next

        if carry:
            result.next = ListNode(carry)

        return dummy.next
