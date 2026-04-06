class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        max1 = 0
        obstacles = set([tuple(i) for i in obstacles])
        x, y = 0, 0
        ls = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0

        for i in commands:
            if (i == -1):
                d = (d + 1) % 4
            elif (i == -2):
                d = (d - 1) % 4
            else:
                for j in range(i):
                    new_x = x + ls[d][0]
                    new_y = y + ls[d][1]

                    if ((new_x, new_y) in obstacles):
                        break
                    
                    x, y = new_x, new_y
                    
                    max1 = max(max1, (x ** 2 + y ** 2))
        
        return max1