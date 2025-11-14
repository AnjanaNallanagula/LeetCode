from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(lambda: 0)
        result = 0
        max1 = 0
        j = 0

        for i in range(len(s)):
            d[s[i]] += 1
            max1 = max(max1, d[s[i]])

            while (j < i and (i - j + 1) > (max1 + k)):
                d[s[j]] -= 1
                j += 1
            
            result = max(result, (i - j + 1))
        
        return result