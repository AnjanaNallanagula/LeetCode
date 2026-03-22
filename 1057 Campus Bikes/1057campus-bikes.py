import heapq

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        m = len(bikes)
        flag1 = [False for i in range(n)]
        flag2 = [False for j in range(m)]
        ls = []
        
        for i in range(n):
            for j in range(m):
                d = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                ls.append((d, i, j))
        
        ls.sort()
        result = [-1 for i in range(n)]
        
        for d, i, j in ls:
            if (flag1[i] == False and flag2[j] == False):
                result[i] = j
                flag1[i] = True
                flag2[j] = True
        
        return result