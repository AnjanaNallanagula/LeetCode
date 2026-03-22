# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def binarySearch(self, mountainArr, low, high, target):
        while (low <= high):
            mid = low + (high - low) // 2
            d = mountainArr.get(mid)
            
            if (d == target):
                return mid
            if (d > target):
                high = mid - 1
            else:
                low = mid + 1
        
        return -1
    
    def binarySearchReverse(self, mountainArr, low, high, target):
        while (low <= high):
            mid = low + (high - low) // 2
            d = mountainArr.get(mid)
            
            if (d == target):
                return mid
            if (d < target):
                high = mid - 1
            else:
                low = mid + 1
        
        return -1
    
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        low = 1
        high = n - 2
        index = -1
        
        while (low <= high):
            mid = low + (high - low) // 2
            d = mountainArr.get(mid)
            d1 = mountainArr.get(mid - 1)
            d2 = mountainArr.get(mid + 1)
            
            if (d > d1 and d > d2):
                index = mid
                break
            if (d2 > d):
                low = mid + 1
            else:
                high = mid - 1
        
        i = self.binarySearch(mountainArr, 0, index, target)
        
        if (i != -1):
            return i
        return self.binarySearchReverse(mountainArr, index + 1, n - 1, target)