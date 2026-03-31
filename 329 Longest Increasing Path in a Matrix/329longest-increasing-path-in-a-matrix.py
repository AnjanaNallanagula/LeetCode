class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        max1 = 0
        ls = [[0 for j in range(m)] for i in range(n)]
        
        def dfs(i, j):
            if (ls[i][j] != 0):
                return ls[i][j]
            
            count = 1
            
            for k in d:
                row = i + k[0]
                col = j + k[1]
                
                if (row >= 0 and row < n and col >= 0 and col < m and matrix[row][col] > matrix[i][j]):
                    count = max(count, 1 + dfs(row, col))
            
            ls[i][j] = count
            
            return count
            
        for i in range(n):
            for j in range(m):
                max1 = max(max1, dfs(i, j))
        
        return max1