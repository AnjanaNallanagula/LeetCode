class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max1 = float("-inf")
        curr_max1 = float("-inf")
        min1 = float("inf")
        curr_min1 = float("inf")
        sum1 = 0

        for i in nums:
            curr_max1 = max(curr_max1 + i, i)
            max1 = max(max1, curr_max1)
            curr_min1 = min(curr_min1 + i, i)
            min1 = min(min1, curr_min1)
            sum1 += i
        
        circular_sum1 = sum1 - min1

        if (min1 == sum1):
            return max1
        
        return max(max1, circular_sum1)