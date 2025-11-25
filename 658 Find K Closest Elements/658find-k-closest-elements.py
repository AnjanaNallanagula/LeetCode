import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = []
        heapq.heapify(q)

        for i in range(len(arr)):
            d = abs(arr[i] - x)
            heapq.heappush(q, (d, arr[i]))
        
        ls = []

        while (k > 0):
            d, n = heapq.heappop(q)
            ls.append(n)
            k -= 1
        
        ls.sort()

        return ls