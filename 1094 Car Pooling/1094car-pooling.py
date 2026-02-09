import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        q = []
        heapq.heapify(q)
        trips.sort(key = lambda i: i[1])

        for i in range(len(trips)):
            heapq.heappush(q, (trips[i][1], 1, trips[i][0]))
            heapq.heappush(q, (trips[i][2], 0, trips[i][0]))
        
        while (len(q) != 0):
            time, flag, count = heapq.heappop(q)

            if (flag == 1):
                if (count > capacity):
                    return False
                
                capacity -= count
            else:
                capacity += count
        
        return True