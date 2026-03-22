from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        j = 0
        max1 = 0

        for i in range(len(s)):
            d[s[i]] += 1

            while (j <= i and d[s[i]] > 1):
                d[s[j]] -= 1
                j += 1
            
            max1 = max(max1, (i - j + 1))
        
        return max1