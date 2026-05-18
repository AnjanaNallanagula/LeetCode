class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        left[0] = nums[0]

        for i in range(1, n):
            left[i] = nums[i] + left[i - 1]
        
        for i in range(n - 2, -1, -1):
            right[i] = left[-1] - left[i]
        
        count = 0

        for i in range(n - 1):
            if (left[i] >= right[i]):
                count += 1
        
        return count