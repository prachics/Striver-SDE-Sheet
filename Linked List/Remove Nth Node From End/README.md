# Problem: Remove Nth Node From End of List

**Leetcode Link:** [Leetcode 19 - Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## Description:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

## Approach:
- Count the total number of nodes.
- Calculate the position from the start: `(length - n)`
- Use a dummy node to handle edge cases easily.
- Traverse and delete the node.

## Time Complexity: O(n)  
## Space Complexity: O(1)

## Tags:
Linked List, Two Pointers
