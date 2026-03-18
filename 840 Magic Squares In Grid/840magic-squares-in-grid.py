class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0

        if (n < 3 or m < 3):
            return 0
        
        def validSum(i, j):
            if (sum(grid[i-1][j-1: j+2]) != 15 or sum(grid[i][j-1: j+2]) != 15 or sum(grid[i+1][j-1: j+2]) != 15):
                return False
            if (sum([grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1]]) != 15 or sum([grid[i-1][j], grid[i][j], grid[i+1][j]]) != 15 or sum([grid[i-1][j+1], grid[i][j+1], grid[i+1][j+1]]) != 15):
                return False
            if (sum([grid[i-1][j-1], grid[i][j], grid[i+1][j+1]]) != 15 or sum([grid[i-1][j+1], grid[i][j], grid[i+1][j-1]]) != 15):
                return False
            return True
        
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if (grid[i][j] == 5):
                    s1 = set()
                    ls1 = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
                    flag1 = True

                    for k in ls1:
                        row = i + k[0]
                        col = j + k[1]

                        if (grid[row][col] < 1 or grid[row][col] > 9 or grid[row][col] % 2 != 0 or grid[row][col] in s1):
                            flag1 = False
                            break
                        
                        s1.add(grid[row][col])
                    
                    if (flag1 == True):
                        s2 = set()
                        ls2 = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                        flag2 = True

                        for k in ls2:
                            row = i + k[0]
                            col = j + k[1]

                            if (grid[row][col] < 1 or grid[row][col] > 9 or grid[row][col] % 2 == 0 or grid[row][col] in s2):
                                flag2 = False
                                break
                            
                            s2.add(grid[row][col])
                
                    if (flag1 == True and flag2 == True and len(s1) + len(s2) == 8 and validSum(i, j) == True):
                        count += 1
        
        return count