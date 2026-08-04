class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ls = [points[0]]
        n = len(points)

        for i in range(1, n):
            if (points[i][0] > ls[-1][1]):
                ls.append(points[i])
            else:
                ls[-1][0] = max(ls[-1][0], points[i][0])
                ls[-1][1] = min(ls[-1][1], points[i][1])
        
        return len(ls)