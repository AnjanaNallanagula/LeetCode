from collections import deque

class Solution:
    def bfs(self, i, j, n, m, grid, s):
        q = deque([])
        q.append((i, j))
        s.add((i, j))
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 1

        while (len(q) != 0):
            d = q.popleft()

            for k in ls:
                row = d[0] + k[0]
                col = d[1] + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= m) or ((row, col) in s) or (grid[row][col] != 1)):
                    continue
                
                q.append((row, col))
                s.add((row, col))
                count += 1
        
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max1 = 0
        n = len(grid)
        m = len(grid[0])
        s = set()

        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 1 and (i, j) not in s):
                    count = self.bfs(i, j, n, m, grid, s)
                    max1 = max(max1, count)
        
        return max1