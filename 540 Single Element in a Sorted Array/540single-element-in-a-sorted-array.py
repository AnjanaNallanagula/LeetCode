class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        if (nums[0] != nums[1]):
            return nums[0]
        if (nums[-1] != nums[-2]):
            return nums[-1]
        
        low = 0
        high = len(nums) - 1

        while (low <= high):
            mid = low + (high - low) // 2

            if (nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
                return nums[mid]

            if ((nums[mid] == nums[mid - 1] and mid % 2 == 0) or (nums[mid] == nums[mid + 1] and mid % 2 != 0)):
                high = mid - 1
            else:
                low = mid + 1