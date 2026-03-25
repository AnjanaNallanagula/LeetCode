class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                total += grid[i][j]
        
        sum1 = 0

        for i in range(n):
            for j in range(m):
                sum1 += grid[i][j]
            
            if ((total - sum1) == sum1):
                return True
        
        sum1 = 0

        for j in range(m):
            for i in range(n):
                sum1 += grid[i][j]
            
            if ((total - sum1) == sum1):
                return True
        
        return False