class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = 0
        for i in nums:
            d = d ^ i
        for i in range(len(nums) + 1):
            d = d ^ i
        return d