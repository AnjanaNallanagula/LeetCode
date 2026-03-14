from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        q = deque()
        n = len(grid)
        s = set()
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(n):
            for j in range(n):
                if (grid[i][j] == 1):
                    q.append((i, j))
                    s.add((i, j))
                    grid[i][j] = 0
        
        while (len(q) != 0):
            i, j = q.popleft()

            for k in ls:
                row = i + k[0]
                col = j + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= n) or ((row, col) in s)):
                    continue
                
                grid[row][col] = grid[i][j] + 1
                q.append((row, col))
                s.add((row, col))
        
        q = []
        heapq.heapify(q)
        heapq.heappush(q, (-grid[0][0], 0, 0))
        s = set()
        s.add((0, 0))

        while (len(q) != 0):
            d, i, j = heapq.heappop(q)
            d *= -1

            if ((i, j) == (n - 1, n - 1)):
                return d
            
            for k in ls:
                row = i + k[0]
                col = j + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= n) or ((row, col) in s)):
                    continue
                
                d1 = min(d, grid[row][col])
                heapq.heappush(q, (-d1, row, col))
                s.add((row, col))