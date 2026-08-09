from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q = deque()
        n = len(rooms)
        m = len(rooms[0])
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(n):
            for j in range(m):
                if (rooms[i][j] == 0):
                    q.append((i, j))
        
        while (len(q) != 0):
            i, j = q.popleft()

            for k in ls:
                row = i + k[0]
                col = j + k[1]

                if ((row < 0 or row >= n) or (col < 0 or col >= m) or (rooms[row][col] != 2147483647)):
                    continue
                
                rooms[row][col] = rooms[i][j] + 1
                q.append((row, col))