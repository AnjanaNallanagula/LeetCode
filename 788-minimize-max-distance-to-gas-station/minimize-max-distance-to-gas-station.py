class Solution:
    def canAllocate(self, stations, n, mid, k):
        count = 0

        for i in range(1, n):
            if (stations[i] - stations[i - 1] > mid):
                count += (stations[i] - stations[i - 1]) // mid
        
        if (count <= k):
            return True
        return False
    
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n = len(stations)
        low = 0
        high = stations[n - 1] - stations[0]
        result = -1

        while (low <= high):
            mid = low + (high - low) / 2

            if (self.canAllocate(stations, n, mid, k)):
                result = mid
                high = mid - 0.000001
            else:
                low = mid + 0.000001
        
        return result