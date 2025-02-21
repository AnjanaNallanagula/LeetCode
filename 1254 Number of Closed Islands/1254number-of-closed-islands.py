class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        s = set()
        d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def islands(i, j, flag):
            if ((i < 0 or i >= n) or (j < 0 or j >= m) or (grid[i][j] != 0) or ((i, j) in s)):
                return
            if ((i == 0 or i == n - 1 or j == 0 or j == m - 1) and (grid[i][j] == 0)):
                flag[0] = True
            s.add((i, j))
            for k in d:
                r = i + k[0]
                c = j + k[1]
                islands(r, c, flag)

        for i in range(n):
            for j in range(m):
                if (i != 0 and i != n - 1 and j != 0 and j != m - 1 and grid[i][j] == 0 and (i, j) not in s):
                    flag = [False]
                    islands(i, j, flag)
                    if (flag[0] == False):
                        count += 1
        
        return count