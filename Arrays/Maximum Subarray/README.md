# Problem: Maximum Subarray

**Leetcode Link:** [Leetcode 53 - Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## Description:
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Approach (Kadane's Algorithm):
- Initialize two variables:
  - `current_sum` = first element
  - `global_sum` = first element
- Traverse the array from the second element:
  - Update `current_sum` as the max of current element and (current element + previous `current_sum`)
  - Update `global_sum` as the max of itself and `current_sum`
- Return `global_sum`

## Time Complexity: O(n)  
## Space Complexity: O(1)

## Tags:
Array, Dynamic Programming, Kadane’s Algorithm
