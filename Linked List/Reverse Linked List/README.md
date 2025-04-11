# Problem: Reverse Linked List

**Leetcode Link:** [Leetcode 206 - Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## Description:
Given the head of a singly linked list, reverse the list and return the reversed list.

## Approach:
- Use three pointers:
  - `prev_ptr` to store the previous node (initially `None`)
  - `head` as the current node
  - `next_ptr` to temporarily store the next node
- At each step:
  - Store `head.next` in `next_ptr`
  - Reverse the link: `head.next = prev_ptr`
  - Move `prev_ptr` and `head` one step forward
- Return `prev_ptr` as the new head of the reversed list

## Time Complexity: O(n)  
## Space Complexity: O(1)

## Tags:
Linked List, Iterative Reversal
