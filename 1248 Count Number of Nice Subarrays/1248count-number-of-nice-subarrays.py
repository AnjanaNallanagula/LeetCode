class Solution:
    def subarraysWithAtmostKOdd(self, nums, k):
        count = 0
        result = 0
        j = 0

        for i in range(len(nums)):
            if (nums[i] % 2 == 1):
                count += 1
            
            while ((j <= i) and (count > k)):
                if (nums[j] % 2 == 1):
                    count -= 1
                j += 1
            
            result += (i - j + 1)
        
        return result

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count1 = self.subarraysWithAtmostKOdd(nums, k)
        count2 = self.subarraysWithAtmostKOdd(nums, k - 1)

        d = count1 - count2

        return d