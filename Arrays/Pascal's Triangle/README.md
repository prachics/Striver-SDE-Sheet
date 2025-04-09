# Problem: Pascal's Triangle

**Leetcode Link:** [Leetcode 118 - Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

## Description:
Given an integer `numRows`, return the first `numRows` of Pascal's Triangle.

In Pascal's Triangle, each number is the sum of the two numbers directly above it.

## Approach:
- Start with the first row `[1]` and build each row based on the previous one.
- For each new row:
  - First and last elements are `1`.
  - Intermediate elements are the sum of two adjacent elements from the previous row.
- Return the resulting list of rows.

## Time Complexity: O(numRows²)  
## Space Complexity: O(numRows²)

## Tags:
Array, Dynamic Programming
