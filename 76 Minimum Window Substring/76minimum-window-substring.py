from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min1 = float("inf")
        s1 = ""
        d = Counter(t)
        need = len(d)
        j = 0

        for i in range(len(s)):
            d[s[i]] -= 1

            if (d[s[i]] == 0):
                need -= 1
            
            while (need == 0):
                if ((i - j + 1) < min1):
                    min1 = i - j + 1
                    s1 = s[j: i+1]
                
                d[s[j]] += 1

                if (d[s[j]] == 1):
                    need += 1
                
                j += 1
        
        return s1