class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        
        while (low <= high):
            mid = low + (high - low) // 2
            d = mid * mid
            
            if (d == num):
                return True
            elif (d > num):
                high = mid - 1
            else:
                low = mid + 1
        
        return False