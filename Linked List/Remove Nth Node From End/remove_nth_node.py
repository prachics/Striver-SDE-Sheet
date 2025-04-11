# Leetcode 19 - Remove Nth Node From End of List
# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1

        temp1 = dummy
        for _ in range(length - n):
            temp1 = temp1.next

        temp1.next = temp1.next.next
        return dummy.next
