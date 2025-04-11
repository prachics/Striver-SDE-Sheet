# Leetcode 206 - Reverse Linked List
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_ptr = None

        while head:
            next_ptr = head.next
            head.next = prev_ptr
            prev_ptr = head
            head = next_ptr

        return prev_ptr
