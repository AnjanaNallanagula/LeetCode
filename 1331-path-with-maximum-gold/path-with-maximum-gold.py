class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ls = [0]
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(i, j, ls, ls1, s):
            ls1[0] += grid[i][j]
            s.add((i, j))

            ls[0] = max(ls[0], ls1[0])

            for k in d:
                row = i + k[0]
                col = j + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= m) or ((row, col) in s) or (grid[row][col] == 0)):
                    continue
                
                dfs(row, col, ls, ls1, s)
            
            ls1[0] -= grid[i][j]
            s.remove((i, j))

        for i in range(n):
            for j in range(m):
                if (grid[i][j] != 0):
                    ls1 = [0]
                    s = set()
                    dfs(i, j, ls, ls1, s)
        
        return ls[0]