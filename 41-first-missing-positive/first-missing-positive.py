class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = len(nums)

        if (nums[0] > 0 and nums[0] != 1):
            return 1
        if (nums[n - 1] < 0):
            return 1

        while (i < n - 1):
            if (nums[i] <= 0 and nums[i + 1] <= 0):
                i += 1
            elif (nums[i] <= 0 and nums[i + 1] > 0 and nums[i + 1] != 1):
                return 1
            elif (nums[i] > 0 and nums[i + 1] > 0 and (nums[i + 1] - nums[i] > 1)):
                return (nums[i] + 1)
            else:
                i += 1
        
        return (nums[n - 1] + 1)