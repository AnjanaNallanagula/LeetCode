class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        result = 0
        
        while (low <= high):
            mid = low + (high - low) // 2
            
            if ((mid * mid) <= x):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result