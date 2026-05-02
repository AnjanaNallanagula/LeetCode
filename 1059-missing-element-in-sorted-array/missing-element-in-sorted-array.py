class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        index = -1
        low = 0
        high = len(nums) - 1
        ls = [0 for i in range(len(nums))]

        for i in range(1, len(nums)):
            ls[i] = abs(nums[i] - nums[i - 1])

            if (ls[i] > 0):
                ls[i] -= 1
            
            ls[i] += ls[i - 1]

        while (low <= high):
            mid = low + (high - low) // 2

            if (ls[mid] < k):
                index = mid
                low = mid + 1
            else:
                high = mid - 1

        d = k - ls[index]

        d1 = nums[index] + d

        return d1