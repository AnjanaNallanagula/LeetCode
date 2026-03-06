class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        j = 0
        p = 1

        for i in range(len(nums)):
            p *= nums[i]

            while (j <= i and p >= k):
                p //= nums[j]
                j += 1
            
            count += (i - j + 1)
        
        return count