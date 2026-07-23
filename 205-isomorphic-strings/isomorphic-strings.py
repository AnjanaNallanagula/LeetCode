from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        d = defaultdict(lambda: 0)
        visited = set()
        n = len(s)
        
        for i in range(len(s)):
            if (s[i] in d and d[s[i]] != t[i]):
                return False
            elif (s[i] not in d and t[i] in visited):
                return False
            d[s[i]] = t[i]
            visited.add(t[i])
        
        return True