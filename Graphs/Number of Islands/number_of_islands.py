# Leetcode 200 - Number of Islands
# Time: O(m * n)
# Space: O(m * n)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            for dr, dc in directions:
                u, v = i + dr, j + dc
                if (u, v) not in visited and 0 <= u < row and 0 <= v < col and grid[u][v] == "1":
                    dfs(u, v)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    dfs(i, j)

        return count
