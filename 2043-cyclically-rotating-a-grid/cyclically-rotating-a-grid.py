class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while (top < bottom and left < right):
            ls = [grid[top][i] for i in range(left, right + 1)]
            ls.extend([grid[i][right] for i in range(top + 1, bottom)])
            ls.extend([grid[bottom][i] for i in range(right, left - 1, -1)])
            ls.extend([grid[i][left] for i in range(bottom - 1, top, -1)])

            d = k % len(ls)
            ls = ls[d:] + ls[:d]
            j = 0

            for i in range(left, right + 1):
                grid[top][i] = ls[j]
                j += 1
            
            for i in range(top + 1, bottom):
                grid[i][right] = ls[j]
                j += 1
            
            for i in range(right, left - 1, -1):
                grid[bottom][i] = ls[j]
                j += 1
            
            for i in range(bottom - 1, top, -1):
                grid[i][left] = ls[j]
                j += 1

            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return grid