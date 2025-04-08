# Problem: Two Sum

**Leetcode Link:** [Leetcode 1 - Two Sum](https://leetcode.com/problems/two-sum/)

## Description:
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Approach:
- Iterate through the list while storing each number's index in a dictionary.
- For each number, check if `target - current_number` exists in the dictionary.
- If it exists, return the indices.
- This solution uses a hash map for constant-time lookup.

## Time Complexity: O(n)  
## Space Complexity: O(n)

## Tags:
Array, Hash Map
