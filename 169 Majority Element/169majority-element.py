class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max1 = -1
        count = 0

        for i in nums:
            if (count == 0):
                max1 = i
                count = 1
            elif (i == max1):
                count += 1
            else:
                count -= 1
        
        count = 0

        for i in nums:
            if (i == max1):
                count += 1
        
        if (count > len(nums) // 2):
            return max1