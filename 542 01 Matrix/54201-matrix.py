from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        s = set()
        n = len(mat)
        m = len(mat[0])
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(n):
            for j in range(m):
                if (mat[i][j] == 0):
                    q.append((i, j, 0))
                    s.add((i, j))
        
        while (len(q) != 0):
            i, j, count = q.popleft()
            mat[i][j] = count

            for k in ls:
                row = i + k[0]
                col = j + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= m) or (mat[row][col] != 1) or ((row, col) in s)):
                    continue
                
                q.append((row, col, count + 1))
                s.add((row, col))
        
        return mat