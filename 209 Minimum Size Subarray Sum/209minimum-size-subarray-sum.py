class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min1 = float("inf")
        j = 0
        sum1 = 0

        for i in range(len(nums)):
            sum1 += nums[i]

            while (j <= i and sum1 >= target):
                if ((i - j + 1) < min1):
                    min1 = (i - j + 1)
                
                sum1 -= nums[j]
                j += 1
            
        if (min1 != float("inf")):
            return min1
        return 0