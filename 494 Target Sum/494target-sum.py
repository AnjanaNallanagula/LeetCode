class Solution:
    def findTargetSumWays1(self, i, sum1, nums, target, d):
        if ((i, sum1) in d):
            return d[(i, sum1)]
        if (i == len(nums) and sum1 == target):
            return 1
        if (i == len(nums)):
            return 0
        
        n1 = self.findTargetSumWays1(i + 1, sum1 + nums[i], nums, target, d)
        n2 = self.findTargetSumWays1(i + 1, sum1 - nums[i], nums, target, d)

        d[(i, sum1)] = n1 + n2

        return d[(i, sum1)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d = {}

        return self.findTargetSumWays1(0, 0, nums, target, d)