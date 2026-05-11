class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        mat = [[0 for j in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(n):
                if (board[i - 1][j] == 1):
                    mat[i][j] += 1
                if (j > 0 and board[i - 1][j - 1] == 1):
                    mat[i][j] += 1
                if (j < n - 1 and board[i - 1][j + 1] == 1):
                    mat[i][j] += 1
        
        for i in range(m - 2, -1, -1):
            for j in range(n):
                if (board[i + 1][j] == 1):
                    mat[i][j] += 1
                if (j > 0 and board[i + 1][j - 1] == 1):
                    mat[i][j] += 1
                if (j < n - 1 and board[i + 1][j + 1] == 1):
                    mat[i][j] += 1
        
        for i in range(m):
            for j in range(1, n):
                if (board[i][j - 1] == 1):
                    mat[i][j] += 1
        
        for i in range(m):
            for j in range(n - 2, -1, -1):
                if (board[i][j + 1] == 1):
                    mat[i][j] += 1
        
        for i in range(m):
            for j in range(n):
                if (board[i][j] == 1 and (mat[i][j] < 2 or mat[i][j] > 3)):
                    board[i][j] = 0
                elif (board[i][j] == 0 and mat[i][j] == 3):
                    board[i][j] = 1