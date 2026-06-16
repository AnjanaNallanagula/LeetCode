from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = defaultdict(lambda: 0)
        j = 0
        max1 = -1

        for i in range(len(s)):
            d[s[i]] += 1

            while (j < i and len(d) > 2):
                d[s[j]] -= 1

                if (d[s[j]] == 0):
                    del d[s[j]]
                
                j += 1
            
            max1 = max(max1, i - j + 1)
        
        return max1