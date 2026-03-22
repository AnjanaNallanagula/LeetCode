class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        
        nums.sort()
        max1 = 1
        count = 1

        for i in range(1, len(nums)):
            if (nums[i] == nums[i - 1] + 1):
                count += 1
            elif (nums[i] != nums[i - 1]):
                max1 = max(max1, count)
                count = 1
        
        max1 = max(max1, count)
        
        return max1