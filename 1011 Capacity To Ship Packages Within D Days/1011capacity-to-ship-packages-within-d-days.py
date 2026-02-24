class Solution:
    def canShip(self, weights, mid, days):
        count = 1
        sum1 = 0

        for i in weights:
            if (sum1 + i > mid):
                count += 1
                sum1 = i
            else:
                sum1 += i
        
        if (count <= days):
            return True
        return False
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        result = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if (self.canShip(weights, mid, days) == True):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result