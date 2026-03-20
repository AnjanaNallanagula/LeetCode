class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ls = [1 for i in range(len(nums))]
        max1 = 1
        
        for i in range(1, len(nums)):
            if (nums[i] > nums[i - 1]):
                ls[i] = ls[i - 1] + 1
            
            max1 = max(max1, ls[i])
        
        return max1