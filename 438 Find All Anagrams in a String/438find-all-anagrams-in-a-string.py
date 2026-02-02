from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = Counter(p)
        need = len(d)
        k = len(p)
        ls = []

        for i in range(len(s)):
            d[s[i]] -= 1

            if (d[s[i]] == 0):
                need -= 1
            
            if (i >= k):
                char = s[i - k]
                d[char] += 1

                if (d[char] == 1):
                    need += 1
            
            if (need == 0):
                ls.append((i - k + 1))
        
        return ls