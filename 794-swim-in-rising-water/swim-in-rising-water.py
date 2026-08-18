import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = []
        heapq.heapify(q)
        heapq.heappush(q, (grid[0][0], 0, 0))
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        s = set()
        s.add((0, 0))

        while q:
            t, i, j = heapq.heappop(q)

            if ((i, j) == (n - 1, n - 1)):
                return t
            
            for r, c in d:
                row = i + r
                col = j + c

                if ((row < 0 or row >= n) or (col < 0 or col >= n) or ((row, col) in s)):
                    continue
                
                heapq.heappush(q, (max(t, grid[row][col]), row, col))
                s.add((row, col))