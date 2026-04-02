class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min1 = float("inf")
        s = set([tuple(i) for i in points])
        n = len(points)
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                point3 = [x1, y2]
                point4 = [x2, y1]
                
                if (point3 != points[i] and point3 != points[j] and point4 != points[i] and point4 != points[j] and tuple(point3) in s and tuple(point4) in s):
                    l = abs(x2 - x1)
                    w = abs(y2 - y1)
                    min1 = min(min1, l * w)
        
        if (min1 != float("inf")):
            return min1
        return 0