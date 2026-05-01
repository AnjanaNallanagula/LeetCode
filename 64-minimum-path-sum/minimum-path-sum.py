class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        mat = [[0 for j in range(m)] for i in range(n)]
        mat[0][0] = grid[0][0]

        for i in range(1, n):
            mat[i][0] = grid[i][0] + mat[i - 1][0]
        
        for j in range(1, m):
            mat[0][j] = grid[0][j] + mat[0][j - 1]
        
        for i in range(1, n):
            for j in range(1, m):
                mat[i][j] = grid[i][j] + min(mat[i - 1][j], mat[i][j - 1])
        
        return mat[n - 1][m - 1]