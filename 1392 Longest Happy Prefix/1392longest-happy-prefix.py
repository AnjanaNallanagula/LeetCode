class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0 for i in range(len(s))]
        
        p = 0
        i = 1
        while (i < len(s)):
            if (s[p] == s[i]):
                lps[i] = p + 1
                p += 1
                i += 1
            elif (p == 0):
                i += 1
            else:
                p = lps[p - 1]
        max1 = 0
        for i in lps:
            max1 = max(max1, i)
        if (max1 != 0):
            return s[:i]
        return ""