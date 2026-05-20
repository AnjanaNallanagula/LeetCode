import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        q = []
        heapq.heapify(q)

        for p, s, e in trips:
            heapq.heappush(q, (s, 1, p))
            heapq.heappush(q, (e, -1, p))
        
        while (len(q) != 0):
            t, d, p = heapq.heappop(q)
            
            if (d == 1):
                capacity -= p
            else:
                capacity += p
            
            if (capacity < 0):
                return False
        
        return True