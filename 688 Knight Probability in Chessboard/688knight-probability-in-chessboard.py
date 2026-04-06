class Solution:
    def knightProbability1(self, n, k, row, col, mat):
        if (k == 0):
            return 1.0
        
        if (mat[row][col][k] != -1):
            return mat[row][col][k]
        
        mat[row][col][k] = 0
        d = 0.0
        ls = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
        
        for l in ls:
            r = row + l[0]
            c = col + l[1]
            
            if (r >= 0 and r < n and c >= 0 and c < n):
                d += self.knightProbability1(n, k - 1, r, c, mat) / 8.0
        
        mat[row][col][k] = d
        
        return mat[row][col][k]
    
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        mat = [[[-1 for l in range(k + 1)] for j in range(n)] for i in range(n)]
        
        return self.knightProbability1(n, k, row, column, mat)