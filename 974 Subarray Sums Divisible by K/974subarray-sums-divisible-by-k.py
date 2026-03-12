from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: 0)
        d[0] = 1
        sum1 = 0
        count = 0

        for i in nums:
            sum1 = (sum1 + i) % k
            count += d[sum1]
            d[sum1] += 1
        
        return count