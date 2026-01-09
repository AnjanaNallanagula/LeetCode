class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while (low < high):
            mid = low + (high - low) // 2

            if (nums[mid] >= target):
                high = mid
            else:
                low = mid + 1
        
        if (target <= nums[low]):
            return low
        return (low + 1)