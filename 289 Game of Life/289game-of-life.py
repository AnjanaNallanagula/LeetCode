class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        d = {0: [0, 0], 1: [1, 0], 2: [0, 1], 3: [1, 0]}
        ls = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                p = board[i][j]
                if (p == 0):
                    count = 0
                    for k, m in ls:
                        row = i + k
                        col = j + m
                        if ((row < 0 or row >= len(board)) or (col < 0 or col >= len(board[0]))):
                            continue
                        if (board[row][col] == 1 or board[row][col] == 3):
                            count += 1
                    if (count == 3):
                        board[i][j] = 2
                else:
                    count = 0
                    for k, m in ls:
                        row = i + k
                        col = j + m
                        if ((row < 0 or row >= len(board)) or (col < 0 or col >= len(board[0]))):
                            continue
                        if (board[row][col] == 1 or board[row][col] == 3):
                            count += 1
                    if (count == 2 or count == 3):
                        board[i][j] = 3
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == 1):
                    board[i][j] = 0
                elif (board[i][j] == 2):
                    board[i][j] = 1
                elif (board[i][j] == 3):
                    board[i][j] = 1
                    
        