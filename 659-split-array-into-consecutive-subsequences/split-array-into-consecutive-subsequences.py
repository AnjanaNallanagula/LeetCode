import heapq
from collections import defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = defaultdict(list)

        for i in nums:
            if d[i-1]:
                min_len = heapq.heappop(d[i-1])
                heapq.heappush(d[i], min_len + 1)
            else:
                heapq.heappush(d[i], 1)
        
        for q in d.values():
            if (q and q[0] < 3):
                return False
        
        return True