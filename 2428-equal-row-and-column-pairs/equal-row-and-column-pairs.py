from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(lambda: 0)

        for i in grid:
            d[tuple(i)] += 1

        for i in range(len(grid)):
            for j in range(i + 1, len(grid)):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

        count = 0

        for i in grid:
            t = tuple(i)
            
            if (t in d):
                count += d[t]

        return count