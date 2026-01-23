class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max1 = float("-inf")

        for i in range(len(nums)):
            if (nums[i] == 1):
                count += 1
            else:
                max1 = max(max1, count)
                count = 0
        
        max1 = max(max1, count)
        
        return max1