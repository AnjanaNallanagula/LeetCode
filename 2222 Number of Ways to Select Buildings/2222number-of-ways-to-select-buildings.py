class Solution:
    def numberOfWays(self, s: str) -> int:
        count_0 = 0
        count_1 = 0

        for i in s:
            if (i == "0"):
                count_0 += 1
            else:
                count_1 += 1
        
        count0 = 0
        count1 = 0
        count = 0

        for i in s:
            if (i == "0"):
                count += count1 * (count_1 - count1)
                count0 += 1
            else:
                count += count0 * (count_0 - count0)
                count1 += 1
        
        return count