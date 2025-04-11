# Problem: Middle of the Linked List

**Leetcode Link:** [Leetcode 876 - Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

## Description:
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

## Approach:
- Use the **two-pointer technique**:
  - Move `slow` by 1 step and `fast` by 2 steps.
  - When `fast` reaches the end, `slow` will be at the middle.
- If the list has an even number of nodes, the second middle is returned by default.

## Time Complexity: O(n)  
## Space Complexity: O(1)

## Tags:
Linked List, Two Pointers
