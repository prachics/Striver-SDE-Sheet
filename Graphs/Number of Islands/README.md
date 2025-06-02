# Problem: Number of Islands

**Leetcode Link:** [Leetcode 200 - Number of Islands](https://leetcode.com/problems/number-of-islands/)

## Description:

Given a 2D grid of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

## Approach:

- Traverse the grid and apply DFS for each unvisited land cell (`"1"`).
- For each DFS traversal starting from a land cell, increment the island count.
- Mark visited cells to avoid revisiting.
- Use direction vectors to explore neighbors (up, down, left, right).

## Time Complexity: O(m \* n)

## Space Complexity: O(m \* n) — for visited set and recursion stack

## Tags:

Graph, DFS, Grid Traversal
