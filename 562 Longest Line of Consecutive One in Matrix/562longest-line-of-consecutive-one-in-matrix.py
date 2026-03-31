class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        ls = [[[0] * 4 for j in range(m)] for i in range(n)]
        max1 = 0

        for i in range(n):
            for j in range(m):
                if (mat[i][j] == 1):
                    ls[i][j][0] = (1 + ls[i][j-1][0]) if (j > 0) else 1
                    ls[i][j][1] = (1 + ls[i-1][j][1]) if (i > 0) else 1
                    ls[i][j][2] = (1 + ls[i-1][j-1][2]) if (i > 0 and j > 0) else 1
                    ls[i][j][3] = (1 + ls[i-1][j+1][3]) if (i > 0 and j < m - 1) else 1
                    d = max(ls[i][j])
                    max1 = max(max1, d)
        
        return max1