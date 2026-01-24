from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)
        q = []
        heapq.heapify(q)
        i = 0
        n = len(s)
        ls = ["" for i in range(n)]

        for k in d:
            heapq.heappush(q, (-1 * d[k], k))
        
        while (len(q) != 0):
            count, d1 = heapq.heappop(q)
            count *= -1

            if (count > (n + 1) // 2):
                return ""

            while (count > 0):
                i = 1 if (i >= n) else i
                ls[i] = d1
                i += 2
                count -= 1
        
        s1 = "".join(ls)

        return s1