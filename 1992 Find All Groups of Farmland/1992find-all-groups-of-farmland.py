from collections import deque
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])
        s = set()
        ls = []
        
        def islands(i, j):
            q = deque()
            q.append((i, j))
            s.add((i, j))
            d = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            while (len(q) != 0):
                r, c = q.popleft()
                flag = False
                for k, p in d:
                    row = r + k
                    col = c + p
                    if ((row < 0 or row >= n) or (col < 0 or col >= m) or ((row, col) in s) or land[row][col] != 1):
                        continue
                    q.append((row, col))
                    s.add((row, col))
                    flag = True
                        
                if (flag == False):
                    r2 = r
                    c2 = c
            return [r2, c2]
                
        for i in range(n):
            for j in range(m):
                if (land[i][j] == 1 and (i, j) not in s):
                    s.add((i, j))
                    p = []
                    p.append(i)
                    p.append(j)
                    r2, c2 = islands(i, j)
                    p.append(r2)
                    p.append(c2)
                    ls.append(p)
        
        return ls
                    