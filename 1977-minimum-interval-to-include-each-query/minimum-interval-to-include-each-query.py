import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        m = len(intervals)

        n = len(queries)
        queries = [(queries[i], i) for i in range(n)]
        queries.sort()

        q = []
        heapq.heapify(q)
        i = 0
        result = [-1 for i in range(n)]

        for val, index in queries:
            while (i < m and intervals[i][0] <= val):
                d = (intervals[i][1] - intervals[i][0] + 1)
                heapq.heappush(q, (d, intervals[i][1]))
                i += 1
            
            while (q and q[0][1] < val):
                heapq.heappop(q)
            
            if q:
                result[index] = q[0][0]
        
        return result