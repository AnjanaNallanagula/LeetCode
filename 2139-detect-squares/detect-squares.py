from collections import defaultdict, Counter

class DetectSquares:

    def __init__(self):
        self.d = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        self.d[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        x, y = point

        if (x not in self.d):
            return 0
        
        result = 0

        for i in self.d:
            if (i == x):
                continue
            
            d1 = abs(i - x)
            result += (self.d[i][y] * self.d[x][y + d1] * self.d[i][y + d1])
            result += (self.d[i][y] * self.d[x][y - d1] * self.d[i][y - d1])
        
        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)