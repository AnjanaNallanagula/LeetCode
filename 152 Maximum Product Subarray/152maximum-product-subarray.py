class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min1 = 1
        max1 = 1
        p = float("-inf")

        for i in nums:
            prev_min = min1
            prev_max = max1

            min1 = min(prev_min * i, prev_max * i, i)
            max1 = max(prev_min * i, prev_max * i, i)
            p = max(p, max1)
        
        return p