import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        heapq.heapify(q)

        if (a > 0):
            heapq.heappush(q, (-a, "a"))
        if (b > 0):
            heapq.heappush(q, (-b, "b"))
        if (c > 0):
            heapq.heappush(q, (-c, "c"))
        
        s = ""

        while (len(q) != 0):
            d, char = heapq.heappop(q)

            if (len(s) >= 2 and char == s[-1] and char == s[-2]):
                if (len(q) == 0):
                    break
                
                d1, char1 = heapq.heappop(q)

                if (-1 * d1 >= 1):
                    s = s + char1
                    d1 += 1
                
                if (d1 < 0):
                    heapq.heappush(q, (d1, char1))
                
                heapq.heappush(q, (d, char))
            else:
                if (-1 * d >= 1):
                    s = s + char
                    d += 1
                
                if (d < 0):
                    heapq.heappush(q, (d, char))
        
        return s