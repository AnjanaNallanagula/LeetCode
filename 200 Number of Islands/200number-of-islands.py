class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        s = set()
        count = 0
        n = len(grid)
        m = len(grid[0])
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(i, j):
            s.add((i, j))

            for k in ls:
                row = i + k[0]
                col = j + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= m) or ((row, col) in s) or (grid[row][col] != "1")):
                    continue
                
                dfs(row, col)
        
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == "1" and (i, j) not in s):
                    dfs(i, j)
                    count += 1
        
        return count