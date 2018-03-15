'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def DFS(grid, x, y, m, n):
            steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            count = 1
            grid[x][y] = 0
            for (i, j) in steps:
                count += DFS(grid, x + i, y + j, m, n)
            return count

        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, DFS(grid, i, j, m, n))
        return res

