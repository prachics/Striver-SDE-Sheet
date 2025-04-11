# Problem: Add Two Numbers

**Leetcode Link:** [Leetcode 2 - Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

## Description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order. Add the two numbers and return the sum as a linked list.

## Approach:
- Traverse both lists.
- Sum corresponding digits and keep track of carry.
- Append result nodes to a dummy linked list.
- At the end, add carry if it's non-zero.

## Time Complexity: O(max(n, m))  
## Space Complexity: O(max(n, m))

## Tags:
Linked List, Math
