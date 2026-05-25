import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        q = []
        heapq.heapify(q)
        ls = sorted(list(zip(capital, profits)))
        j = 0

        for i in range(k):
            while (j < len(ls) and ls[j][0] <= w):
                heapq.heappush(q, -ls[j][1])
                j += 1
            
            if (len(q) == 0):
                break
            
            d = -1 * heapq.heappop(q)
            w += d
        
        return w