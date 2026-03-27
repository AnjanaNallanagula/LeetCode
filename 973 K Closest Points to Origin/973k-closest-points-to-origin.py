import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        heapq.heapify(q)
        
        for x, y in points:
            d = (x ** 2 + y ** 2) ** 0.5
            heapq.heappush(q, (d, [x, y]))
        
        ls = []
        
        while (len(q) != 0 and k > 0):
            d, point = heapq.heappop(q)
            ls.append(point)
            k -= 1
        
        return ls