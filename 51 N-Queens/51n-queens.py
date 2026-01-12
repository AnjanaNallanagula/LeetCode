class Solution:
    def isSafe(self, row, col, board, n):
        for i in range(row - 1, -1, -1):
            if (board[i][col] == "Q"):
                return False
        
        for j in range(col - 1, -1, -1):
            if (board[row][j] == "Q"):
                return False
        
        i = row - 1
        j = col - 1

        while (i >= 0 and j >= 0):
            if (board[i][j] == "Q"):
                return False
            
            i -= 1
            j -= 1
        
        i = row - 1
        j = col + 1

        while (i >= 0 and j < n):
            if (board[i][j] == "Q"):
                return False
            
            i -= 1
            j += 1
        
        return True
    
    def solveNQueens1(self, row, board, n, ls):
        if (row == n):
            ls1 = []

            for i in board:
                s = "".join(i)
                ls1.append(s)
            
            ls.append(ls1[:])
            return
        
        for j in range(n):
            if (self.isSafe(row, j, board, n) == True):
                board[row][j] = "Q"
                self.solveNQueens1(row + 1, board, n, ls)
                board[row][j] = "."
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for j in range(n)] for i in range(n)]
        ls = []

        self.solveNQueens1(0, board, n, ls)

        return ls