from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        min1 = float("inf")
        ls = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        s = set()
        s.add(tuple(entrance))

        while (len(q) != 0):
            i, j, d = q.popleft()

            for k in ls:
                row = i + k[0]
                col = j + k[1]

                if ((row < 0 or row >= len(maze)) or (col < 0 or col >= len(maze[0])) or ((row, col) in s) or (maze[row][col] != ".")):
                    continue
                
                if ((row == 0 or row == len(maze) - 1) or (col == 0 or col == len(maze[0]) - 1)):
                    min1 = min(min1, d + 1)
                
                q.append((row, col, d + 1))
                s.add((row, col))
        
        if (min1 != float("inf")):
            return min1
        return -1