# Problem: Sort Colors

**Leetcode Link:** [Leetcode 75 - Sort Colors](https://leetcode.com/problems/sort-colors/)

## Description:
Given an array `nums` with `n` objects colored red (0), white (1), or blue (2), sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red → white → blue.

## Approach:
- Count the number of 0s, 1s, and 2s in the array.
- Overwrite the array by placing 0s, then 1s, then 2s based on their counts.
- This is known as the **Counting Sort** method and is suitable when the range of values is small and known.

Time Complexity: O(n)
Space Complexity: O(1)