from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = Counter(s1)
        need = len(d)
        k = len(s1)
        
        for i in range(len(s2)):
            d[s2[i]] -= 1

            if (d[s2[i]] == 0):
                need -= 1
            
            if (i >= k):
                d[s2[i-k]] += 1

                if (d[s2[i-k]] == 1):
                    need += 1
            
            if (need == 0):
                return True
        
        return False