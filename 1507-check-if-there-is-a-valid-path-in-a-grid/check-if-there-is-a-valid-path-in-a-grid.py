from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        q = deque([])
        q.append((0, 0, grid[0][0]))
        n = len(grid)
        m = len(grid[0])
        s = set()
        s.add((0, 0))
        d = {1: [[0, -1], [0, 1]], 2: [[-1, 0], [1, 0]], 3: [[0, -1], [1, 0]], 4: [[0, 1], [1, 0]], 5: [[0, -1], [-1, 0]], 6: [[0, 1], [-1, 0]]}

        while (len(q) != 0):
            i, j, val = q.popleft()

            if ((i, j) == (n - 1, m - 1)):
                return True

            for r, c in d[val]:
                row = i + r
                col = j + c
            
                if ((row < 0 or row >= n) or (col < 0 or col >= m) or ((row, col) in s)):
                    continue
                
                if ([-r, -c] in d[grid[row][col]]):
                    q.append((row, col, grid[row][col]))
                    s.add((row, col))
        
        return False