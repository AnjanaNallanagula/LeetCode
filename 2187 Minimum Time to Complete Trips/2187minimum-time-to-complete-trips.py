class Solution:
    def canComplete(self, time, totalTrips, mid):
        count = 0

        for i in time:
            count += (mid // i)
        
        if (count >= totalTrips):
            return True
        return False
    
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low = 1
        high = (min(time) * totalTrips)
        result = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if (self.canComplete(time, totalTrips, mid) == True):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result