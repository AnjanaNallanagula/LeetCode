import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        for i in range(len(queries)):
            queries[i] = (queries[i], i)
        
        queries.sort()
        ls = [-1 for i in range(len(queries))]
        i = 0
        q = []
        heapq.heapify(q)

        for j in range(len(queries)):
            while (i < len(intervals) and intervals[i][0] <= queries[j][0]):
                d = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(q, (d, intervals[i][1]))
                i += 1
            
            while (len(q) != 0 and q[0][1] < queries[j][0]):
                heapq.heappop(q)
            
            if (len(q) != 0):
                ls[queries[j][1]] = q[0][0]
        
        return ls