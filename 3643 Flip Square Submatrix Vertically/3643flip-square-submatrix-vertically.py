class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        row = x + k - 1
        col = y + k - 1

        for j in range(y, col + 1):
            top = x
            bottom = row

            while (top < bottom):
                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]
                top += 1
                bottom -= 1
        
        return grid