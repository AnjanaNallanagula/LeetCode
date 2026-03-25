class Solution:
    def getMoneyAmount(self, n: int) -> int:
        mat = [[0 for j in range(n + 1)] for i in range(n + 1)]
        
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                mat[i][j] = j + mat[i][j - 1]
                
                for k in range(i, j):
                    mat[i][j] = min(mat[i][j], k + max(mat[i][k - 1], mat[k + 1][j]))
        
        return mat[1][n]