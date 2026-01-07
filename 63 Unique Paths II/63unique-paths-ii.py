from collections import deque

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if (obstacleGrid[0][0] == 1):
            return 0
        
        q = deque([])
        q.append((0, 0))
        ls = [[0, 1], [1, 0]]
        mat = [[0 for j in range(m)] for i in range(n)]
        mat[0][0] = 1

        while (len(q) != 0):
            i, j = q.popleft()
            
            for k in ls:
                row = i + k[0]
                col = j + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= m) or (obstacleGrid[row][col] == 1)):
                    continue
                
                if (mat[row][col] == 0):
                    q.append((row, col))
                
                mat[row][col] += mat[i][j]
        
        return mat[n - 1][m - 1]