class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sum1 = 0
        d = {nums[0]: 0}
        max1 = float("-inf")
        n = len(nums)
        
        for i in range(n):
            sum1 += nums[i]

            if (nums[i] - k in d):
                max1 = max(max1, sum1 - d[nums[i] - k])
            if (nums[i] + k in d):
                max1 = max(max1, sum1 - d[nums[i] + k])

            if ((i + 1 < n) and (nums[i + 1] not in d or d[nums[i + 1]] > sum1)):
                d[nums[i + 1]] = sum1

        if (max1 != float("-inf")):
            return max1
        return 0