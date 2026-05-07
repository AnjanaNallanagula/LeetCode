class Solution:
    def canPlace(self, position, mid, m):
        count = 1
        prev = position[0]

        for i in range(1, len(position)):
            if (position[i] - prev >= mid):
                prev = position[i]
                count += 1
        
        if (count >= m):
            return True
        return False
    
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low = 1
        high = position[-1] - position[0]
        result = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if (self.canPlace(position, mid, m) == True):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result