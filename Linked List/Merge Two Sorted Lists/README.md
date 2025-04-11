# Problem: Merge Two Sorted Lists

**Leetcode Link:** [Leetcode 21 - Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## Description:
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

## Approach:
- Use a dummy node to start the merged list.
- Compare nodes from both lists and attach the smaller one.
- After the loop, attach the remaining nodes from the non-empty list.

## Time Complexity: O(n + m)  
## Space Complexity: O(1)

## Tags:
Linked List, Merge, Iteration
