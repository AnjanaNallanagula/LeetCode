class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min1 = float("inf")

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if (nums[i] == nums[j] and nums[i] == nums[k]):
                        d = abs(i - j) + abs(i - k) + abs(j - k)
                        min1 = min(min1, d)
        
        if (min1 != float("inf")):
            return min1
        return -1