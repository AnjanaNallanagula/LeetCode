from collections import deque

class Solution:
    def bfs(self, i, j, n, m, board, s):
        q = deque([])
        q.append((i, j))
        s.add((i, j))
        ls1 = []
        ls1.append((i, j))
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while (len(q) != 0):
            d = q.popleft()

            if (d[0] == 0 or d[0] == (n - 1) or d[1] == 0 or d[1] == (m - 1)):
                ls1 = []
            
            for k in ls:
                row = d[0] + k[0]
                col = d[1] + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= m) or ((row, col) in s) or (board[row][col] != "O")):
                    continue
                
                q.append((row, col))
                s.add((row, col))

                if (ls1 != []):
                    ls1.append([row, col])
        
        for i in ls1:
            board[i[0]][i[1]] = "X"

    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        s = set()

        for i in range(n):
            for j in range(m):
                if (board[i][j] == "O" and (i, j) not in s):
                    self.bfs(i, j, n, m, board, s)