from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: 0)
        count = 0
        j = 0
        result = 0

        for i in range(len(nums)):
            count += d[nums[i]]
            d[nums[i]] += 1

            while (count >= k):
                d[nums[j]] -= 1
                count -= d[nums[j]]
                j += 1
            
            result += j
        
        return result