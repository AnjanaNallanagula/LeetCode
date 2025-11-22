from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        d = defaultdict(lambda: 0)
        d1 = defaultdict(lambda: 0)
        j = 0
        max1 = 0

        for i in range(len(s)):
            d[s[i]] += 1

            if ((i - j + 1) > minSize):
                d[s[j]] -= 1

                if (d[s[j]] == 0):
                    del d[s[j]]
                
                j += 1
            
            if (((i - j + 1) == minSize) and (len(d) <= maxLetters)):
                s1 = s[j: i + 1]
                d1[s1] += 1
                max1 = max(max1, d1[s1])

        return max1